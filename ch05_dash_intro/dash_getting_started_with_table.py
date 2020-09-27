import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
from dash_table import DataTable

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

gapminder = px.data.gapminder()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        html.H3("左側のグラフの要素をShift+マウスクリックで複数国が選択できます。"),
        html.Div(
            [
                dcc.Graph(
                    id="graph1",
                    figure=px.scatter(
                        gapminder,
                        x="gdpPercap",
                        y="lifeExp",
                        size="pop",
                        color="continent",
                        animation_frame="year",
                        log_x=True,
                        size_max=70,
                        range_y=[20, 90],
                        hover_data=["country"],
                        template={"layout": {"clickmode": "event+select"}},
                    ),
                    style={"width": "50%", "display": "inline-block", "height": 600},
                ),
                html.Div(
                    [
                        dcc.Graph(id="graph2", style={"height": 300}),
                        dcc.Graph(id="graph3", style={"height": 300}),
                    ],
                    style={"width": "50%", "display": "inline-block", "height": 600},
                ),
            ]
        ),
        html.Div(
            [DataTable(id="table", export_format="csv", filter_action="native"),],
            style={"width": "80%", "margin": "auto"},
        ),
    ]
)


@app.callback(
    Output("graph2", "figure"),
    Output("graph3", "figure"),
    Output("table", "columns"),
    Output("table", "data"),
    Input("graph1", "selectedData"),
)
def update_graph(selectedData):
    if selectedData:
        selected_countries = [data["customdata"][0] for data in selectedData["points"]]
        selected_df = gapminder[gapminder["country"].isin(selected_countries)]
        fig1 = px.line(selected_df, x="year", y="pop", color="country", title="各国の人口")
        fig2 = px.line(
            selected_df, x="year", y="gdpPercap", color="country", title="各国の1人当たりGDP"
        )
        columns = [
            {"name": col, "id": col, "deletable": True} for col in selected_df.columns
        ]
        return fig1, fig2, columns, selected_df.to_dict("records")
    raise dash.exceptions.PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)
