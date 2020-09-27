import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# タイトルとドロップダウンを作成するコンポーネント
def header_and_dropdown(header_name, columns_name, dropdown_id):
    return html.Div(
        [
            html.H2(header_name),
            dcc.Dropdown(
                id=dropdown_id,
                options=[{"label": col, "value": col} for col in columns_name],
                value=columns_name[0],
            ),
        ],
        style={"width": "49%", "display": "inline-block"},
    )


gapminder = px.data.gapminder()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    [
        html.H1("Gapminder Graph"),
        html.Div(
            [
                header_and_dropdown("Select X axis", gapminder.columns[3:6], "x_axis"),
                header_and_dropdown("Select Y axis", gapminder.columns[3:6], "y_axis"),
            ]
        ),
        dcc.Graph(id="graph"),
    ]
)

# コールバック
@app.callback(
    Output("graph", "figure"), Input("x_axis", "value"), Input("y_axis", "value")
)
def update_graph(x_axis_value, y_axis_value):
    return px.scatter(
        gapminder,
        x=x_axis_value,
        y=y_axis_value,
        color="country",
        log_x=True,
        log_y=True,
    )


if __name__ == "__main__":
    app.run_server(debug=True)
