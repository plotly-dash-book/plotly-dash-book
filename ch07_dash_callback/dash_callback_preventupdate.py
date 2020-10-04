import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

gapminder = px.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        dcc.Graph(
            id="gapminder-g",
            figure=px.scatter(
                gapminder2007, x="gdpPercap", y="lifeExp", hover_name="country"
            ),
        ),
        html.P(
            id="hoverdata-p",
            style={
                "fontSize": 24,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#e1eef6",
            },
        ),
        # コールバックの出力先
        html.P(
            id="prevent-p",
            style={
                "fontSize": 24,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#D7FFF1",
            },
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)

# PreventUpdateを用いないコールバック
@app.callback(Output("hoverdata-p", "children"), Input("gapminder-g", "hoverData"))
def show_hover_data(hoverData):
    return json.dumps(hoverData)


# ➊ PreventUpdateを用いたコールバック
@app.callback(Output("prevent-p", "children"), Input("gapminder-g", "hoverData"))
def prevent_none(hoverData):
    if hoverData is None:
        # ➋ PreventUpdateクラスを用いて更新を停止
        raise dash.exceptions.PreventUpdate
    return json.dumps(hoverData)


if __name__ == "__main__":
    app.run_server(debug=True)
