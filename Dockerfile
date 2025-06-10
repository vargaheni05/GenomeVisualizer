FROM python:3.13-slim

WORKDIR /toolbox

# install fonts for the logo
RUN apt-get update
RUN apt-get install -y git &&  \
    git clone --depth 1 https://github.com/ryanoasis/nerd-fonts.git && \
    cd nerd-fonts && \
    ./install.sh BigBlueTerminal && \
    cd .. && rm -rf nerd-fonts

RUN pip install gunicorn

COPY . .
RUN pip install ./ToolBox/
RUN pip install -r ./ToolBoxWeb/requirements.txt

ENV PORT 8000

ENTRYPOINT [ "gunicorn", "--timeout", "128", "-k", "uvicorn.workers.UvicornWorker", "ToolBoxWeb.main:app", "--log-level=info", "--access-logfile=-" ]

