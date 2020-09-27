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
        html.Div(
            [
                dcc.Graph(id="graph1", className="six columns"),
                dcc.Graph(id="graph2", className="six columns"),
            ]
        ),
    ],
    style={"width": "80%", "margin": "auto", "textAlign": "center"},
)


@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Input("gapminder-g", "selectedData"),
)
def show_hover_data(selectedData):
    if selectedData:
        selected_countries = [data["hovertext"] for data in selectedData["points"]]
        selected_df = gapminder[gapminder["country"].isin(selected_countries)]
        fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
        fig2 = px.line(
            selected_df, x="year", y="lifeExp", color="country", title="各国の平均寿命"
        )
        return fig1, fig2
    raise dash.exceptions.PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)
