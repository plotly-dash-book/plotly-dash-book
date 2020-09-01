import time

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H3("Loading_Test"),
        dcc.Textarea(id="input_text", value="最初の値"),
        html.Button(id="input_1", children="Push"),
        # ➊ コールバックの出力先のDivを管理するLoadingコンポーネントを設定する
        dcc.Loading(
            id="loading_1",
            type="cube",
            children=[html.H1(id="loading", style={"margin": 100})],
        ),
    ],
    style={"textAlign": "center"},
)

# ➋ コールバック
@app.callback(
    Output("loading", "children"),
    [Input("input_1", "n_clicks")],
    [State("input_text", "value")],
)
def input_trigger_spinner(n_clicks, value):
    time.sleep(3)
    return value


if __name__ == "__main__":
    app.run_server(debug=True)
