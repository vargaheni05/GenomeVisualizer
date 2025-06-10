FROM python:3.13-slim

WORKDIR /toolbox
RUN apt-get install -y ttf-mscorefonts-installer
RUN pip install gunicorn

COPY . .
RUN pip install ./ToolBox/
RUN pip install -r ./ToolBoxWeb/requirements.txt

ENV PORT 8000

ENTRYPOINT [ "gunicorn", "--timeout", "128", "-k", "uvicorn.workers.UvicornWorker", "ToolBoxWeb.main:app", "--log-level=info", "--access-logfile=-" ]

