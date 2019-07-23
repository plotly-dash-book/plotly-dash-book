FROM python:3.7.4-slim-stretch

WORKDIR /work

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    curl https://raw.githubusercontent.com/plotly-dash-book/plotly-dash-book/master/requirements.txt -o /work/requirements.txt && \
    apt-get install -y nodejs && \
    pip install -r /work/requirements.txt && \
    export NODE_OPTIONS=--max-old-space-size=4096 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.0 --no-build && \
    jupyter labextension install jupyterlab-plotly@1.0.0 --no-build && \
    jupyter labextension install plotlywidget@1.0.0 --no-build && \
    jupyter labextension install jupyterlab-chart-editor@1.2 --no-build && \
    jupyter lab build && \
    unset NODE_OPTIONS
