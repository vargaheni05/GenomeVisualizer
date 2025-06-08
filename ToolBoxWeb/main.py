import pathlib
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

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


@app.get("/feature", response_class=HTMLResponse)
def feature_page(request: Request, feature: int):
    try:
        selected_feature = features[feature]
    except IndexError:
        raise HTTPException(
            status_code=400,
            detail=f"Feauture index {feature} out of range. Expected between {0} and {len(features)}",
        )
    return templates.TemplateResponse(selected_feature.template, {"request": request})
