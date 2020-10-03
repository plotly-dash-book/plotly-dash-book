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
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#e1eef6",
            },
        ),
        html.P(
            id="prevent-p",
            style={
                "fontSize": 32,
                "textAlign": "center",
                "height": 100,
                "backgroundColor": "#D7FFF1",
            },
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


@app.callback(
    # ➊ データの状態に関係なくコールバックを更新する出力先
    Output("hoverdata-p", "children"),
    # ➋ Noneであれば、コールバックの更新を停止する出力先
    Output("prevent-p", "children"),
    Input("gapminder-g", "hoverData"),
)
def show_hover_data(hoverData):
    if hoverData is None:
        # ➌ 1つ目の戻り値はホバーデータをそのまま、2つ目の戻り値は更新を停止
        return (json.dumps(hoverData), dash.no_update)
    return json.dumps(hoverData), json.dumps(hoverData)


if __name__ == "__main__":
    app.run_server(debug=True)
