import io
import os
import json
import logging
import pathlib
import tempfile
from typing import Annotated
from fastapi import (
    BackgroundTasks,
    FastAPI,
    Form,
    Request,
    Response,
    UploadFile,
)
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
    logging.exception("Unhandled exception", exc_info=exc)
    return error_page(request, repr(exc))


@app.exception_handler(RequestValidationError)
async def handle_request_validation_exceptions(request, exc):
    logging.exception("Request validation failed", exc_info=exc)
    return error_page(
        request,
        "\n".join(
            f'Invalid input ({'.'.join(e['loc'][1:])}): {e["msg"]}'
            for e in exc.errors()
        ),
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
    Tool(name="Skew", template="skew.html"),
    Tool(name="Symbol", template="symbol.html"),
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


class GenomeInput(BaseModel):
    pattern: str | UploadFile

    @field_validator("pattern")
    def text_has_appropriate_alphabet(cls, v):
        if not isinstance(v, str):
            return v
        return ensure_genome(v)


@app.post("/reverse-complement")
async def reverse_complement_page(
    request: Request, input: Annotated[GenomeInput, Form()]
):
    genome = input.pattern
    if not isinstance(genome, str):
        genome = (await genome.read()).decode()
        genome = ensure_genome(genome)
    result = GenomeVisualizer.ReverseComplement(genome)
    return templates.TemplateResponse(
        "reverse_complement_result.html", {"request": request, "result": result}
    )


class SymbolInput(BaseModel):
    genome: str | UploadFile
    symbol: str

    @field_validator("symbol")
    def symbol_is_valid(cls, v: str):
        if len(v) != 1:
            raise ValueError('`symbol` must be one of {"A", "T", "C", "G"}')
        v = v.upper()
        if v not in {"A", "T", "C", "G"}:
            raise ValueError('`symbol` must be one of {"A", "T", "C", "G"}')
        return v

    @field_validator("genome")
    def genome_has_appropriate_alphabet(cls, v):
        if not isinstance(v, str):
            return v
        return ensure_genome(v)


def ensure_genome(v) -> str:
    if not v:
        raise ValueError("`pattern` can't be empty")
    # remove all whitespace
    v = "".join(v.split()).upper()
    letters = set(v)
    extra_chars = letters - {"A", "T", "C", "G"}
    if extra_chars:
        raise ValueError(
            f"Invalid characters in input: {', '.join(extra_chars)}. Only 'A', 'T', 'C', and 'G' characters are accepted."
        )
    return v


@app.get("/img")
async def get_image(request: Request, fname: str, bg: BackgroundTasks):
    img_buf = open(fname, "rb")
    bg.add_task(img_buf.close)
    return Response(
        img_buf.read(),
        headers={"Content-Disposition": f'inline; filename="{fname}"'},
        media_type="image/png",
    )


@app.post("/skew")
async def skew_page(request: Request, input: Annotated[GenomeInput, Form()]):
    genome = input.pattern
    if not isinstance(genome, str):
        genome = (await genome.read()).decode()
        genome = ensure_genome(genome)

    skew_array = GenomeVisualizer.SkewArray(genome)
    min_skew = GenomeVisualizer.basic.MinPositions(skew_array)

    label = ""
    if not isinstance(input.pattern, str):
        label, _ = os.path.splitext(input.pattern.filename)
    fig: Figure = GenomeVisualizer.visualization.plot_skew_array_with_ori_impl(
        skew_array, min_skew, genome_label=label
    )
    with tempfile.NamedTemporaryFile(
        suffix=".png", delete=False, delete_on_close=False
    ) as f:
        skew_array_img = f.name
        fig.savefig(f, format="png")

    return templates.TemplateResponse(
        "skew_result.html",
        {
            "request": request,
            "skew_array_img": skew_array_img,
        },
    )


@app.post("/symbol")
async def symbol_page(request: Request, input: Annotated[SymbolInput, Form()]):
    genome = input.genome
    if not isinstance(genome, str):
        genome = (await genome.read()).decode()
        genome = ensure_genome(genome)

    symbol_array = GenomeVisualizer.FasterSymbolArray(genome, input.symbol)

    label = ""
    if not isinstance(input.genome, str):
        label, _ = os.path.splitext(input.genome.filename)

    fig: Figure = GenomeVisualizer.visualization.plot_symbol_array_impl(
        symbol_array, input.symbol, genome_label=label
    )
    with tempfile.NamedTemporaryFile(
        suffix=".png", delete=False, delete_on_close=False
    ) as f:
        symbol_array_img = f.name
        fig.savefig(f, format="png")

    return templates.TemplateResponse(
        "symbol_result.html",
        {
            "request": request,
            "symbol_array_img": symbol_array_img,
        },
    )
