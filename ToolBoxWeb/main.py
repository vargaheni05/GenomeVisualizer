import io
import logging
import pathlib
from typing import Any
from fastapi import BackgroundTasks, FastAPI, Form, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from matplotlib.figure import Figure
from pydantic import BaseModel
import GenomeVisualizer
import matplotlib.pyplot as plt


HERE = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=HERE / "templates")


# adding a new Feauture:
# - fill out the methods with the new name
# - create feature specific templates
# - add a Feauture instance with the name to the features list


class Feature(BaseModel):
    name: str
    # relative path of the template file
    template: str


features: list[Feature] = [Feature(name="Pr", template="pr.html")]


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


class PrInput(BaseModel):
    text: str
    # TODO: accept profile as JSON?
    profile: dict[str, list[Any]] = {}


@app.post("/pr", response_class=HTMLResponse)
def pr_page(request: Request, input: PrInput = Form()):
    try:
        result = GenomeVisualizer.Pr(input.text, input.profile)
    except Exception as err:
        logging.exception("Failed to process Pr")
        return error_page(
            request,
            f"Failed to process Pr of input: {repr(err)}",
        )
    return templates.TemplateResponse(
        "pr_result.html", {"request": request, "result": result}
    )


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
