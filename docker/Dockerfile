FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y npm nodejs && \
    pip install -r https://raw.githubusercontent.com/plotly-dash-book/plotly-dash-book/master/requirements.txt && \
    jupyter labextension install jupyterlab-plotly@4.10.0 && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.10.0

ENV JUPYTER_CONFIG=/root/.jupyter/jupyter_notebook_config.py

RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> ${JUPYTER_CONFIG} && \
    echo "c.NotebookApp.open_browser = False" >> ${JUPYTER_CONFIG} && \
    echo "c.NotebookApp.allow_root = True" >> ${JUPYTER_CONFIG} && \
    echo "c.NotebookApp.notebook_dir = '/work'" >> ${JUPYTER_CONFIG}

WORKDIR /work