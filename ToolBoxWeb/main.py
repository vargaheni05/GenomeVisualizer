import io
import string
import pathlib
from typing import Any
from fastapi import BackgroundTasks, FastAPI, Form, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from matplotlib.figure import Figure
from pydantic import BaseModel, field_validator
import GenomeVisualizer
import matplotlib.pyplot as plt


HERE = pathlib.Path(__file__).parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.exception_handler(Exception)
async def handle_exceptions(request, exc):
    return error_page(request, repr(exc))


@app.exception_handler(RequestValidationError)
async def handle_http_exceptions(request, exc):
    return error_page(
        request,
        "\n".join(f'Invalid input: {e["msg"]}' for e in exc.errors()),
    )


# adding a new Feauture:
# - fill out the methods with the new name
# - create feature specific templates
# - add a Feauture instance with the name to the features list


class Tool(BaseModel):
    name: str
    # relative path of the template file
    template: str


features: list[Tool] = [
    Tool(name="Reverse Complement", template="reverse_complement.html"),
]


@app.get("/", response_class=HTMLResponse)
def index_page(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "features": features}
    )


def error_page(request, error):
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "error": error,
        },
    )


@app.get("/feature", response_class=HTMLResponse)
def feature_page(request: Request, feature: int):
    try:
        selected_feature = features[feature]
    except IndexError:
        return error_page(
            request,
            f"Feauture index {feature} out of range. Expected between {0} and {len(features)}",
        )
    return templates.TemplateResponse(selected_feature.template, {"request": request})


def make_image_response(figure: Figure, bg: BackgroundTasks, fname="out.png"):
    """
    @param bg: Image buffers are closed using BackgroundTasks so we don't leak memory
    """
    img_buf = io.BytesIO()
    figure.savefig(img_buf, format="png")
    bg.add_task(img_buf.close)
    return Response(
        img_buf.getvalue(),
        headers={"Content-Disposition": f'inline; filename="{fname}"'},
        media_type="image/png",
    )


@app.get("/test-image")
def image_response_test(bg: BackgroundTasks):
    fig = plt.figure()
    plt.plot([1, 2, 3], [1, 5, 2])
    return make_image_response(fig, bg)


class ReverseComplementInput(BaseModel):
    pattern: str

    @field_validator("pattern")
    def text_has_appropriate_alphabet(cls, v: str):
        if not v:
            raise ValueError("`pattern` can't be empty")
        v = v.upper()
        letters = set(c for c in v if c not in string.whitespace)
        extra_chars = letters - {"A", "T", "C", "G"}
        if extra_chars:
            raise ValueError(
                f"Invalid characters in input: {', '.join(extra_chars)}. Only 'A', 'T', 'C', and 'G' characters are accepted."
            )
        return v


@app.post("/reverse-complement")
def reverse_complement_page(request: Request, input: ReverseComplementInput = Form()):
    result = GenomeVisualizer.ReverseComplement(input.pattern)
    return templates.TemplateResponse(
        "reverse_complement_result.html", {"request": request, "result": result}
    )
