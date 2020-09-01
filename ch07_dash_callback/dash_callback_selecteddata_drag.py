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
                gapminder2007,
                x="gdpPercap",
                y="lifeExp",
                hover_name="country",
                # ➊ ドラッグモードを"select"に
                template={"layout": {"dragmode": "select"}},
            ),
        ),
        html.P(id="hoverdata-p", style={"fontSize": 32, "textAlign": "center"}),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


@app.callback(Output("hoverdata-p", "children"), [Input("gapminder-g", "selectedData")])
def show_hover_data(selectedData):
    return json.dumps(selectedData)


if __name__ == "__main__":
    app.run_server(debug=True)
