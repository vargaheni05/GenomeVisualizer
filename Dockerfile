FROM python:3.13-slim


WORKDIR /fonts
# install fonts for the logo
RUN apt-get update
RUN apt-get install -y curl zip unzip fontconfig &&  \
    curl -OL 'https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/BitstreamVeraSansMono.zip' && \
    unzip BitstreamVeraSansMono.zip -d fonts && \
    mkdir -p ~/.fonts && \
    mv fonts/* ~/.fonts && \
    fc-cache -fv

WORKDIR /toolbox
RUN pip install gunicorn

COPY . .
RUN pip install ./ToolBox/
RUN pip install -r ./ToolBoxWeb/requirements.txt

ENV PORT 8000

ENTRYPOINT [ "gunicorn", "--timeout", "128", "-k", "uvicorn.workers.UvicornWorker", "ToolBoxWeb.main:app", "--log-level=info", "--access-logfile=-" ]

