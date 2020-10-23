import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ➊ レイアウト
app.layout = html.Div(
    [
        html.Div(
            [
                daq.PowerButton(
                    id="daq-powerbutton",
                    label="計器を動作させるボタン",
                    on=False,
                    size=100,
                    color="red",
                ),
                dcc.Interval(id="daq-interval", interval=1000, n_intervals=0),
            ]
        ),
        # ➍ 計器を並べる
        html.Div(
            [
                html.Div(
                    [html.H2("ゲージ"), daq.Gauge(id="guage1")], className="three columns",
                ),
                html.Div(
                    [html.H2("グラデュエートバー"), daq.GraduatedBar(id="guage2")],
                    className="three columns",
                ),
                html.Div(
                    [html.H2("タンク"), daq.Tank(id="guage3")], className="three columns",
                ),
                html.Div(
                    [html.H2("LEDディスプレイ"), daq.LEDDisplay(id="guage4")],
                    className="three columns",
                ),
            ],
            style={"margin": "auto"},
        ),
    ]
)

# ➋ コールバック オンとオフを管理するコールバック
@app.callback(Output("daq-interval", "disabled"), Input("daq-powerbutton", "on"))
def guage_witch(buttonon):
    if buttonon:
        return False
    else:
        return True


# ➌ コールバック 計器にランダムな値を返すコールバック
@app.callback(
    Output("guage1", "value"),
    Output("guage2", "value"),
    Output("guage3", "value"),
    Output("guage4", "value"),
    Input("daq-interval", "n_intervals"),
)
def update_guages(n_intervals):
    return list(np.random.uniform(0, 10, 4))


if __name__ == "__main__":
    app.run_server(debug=True)
