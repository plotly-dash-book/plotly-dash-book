import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

# gapminderデータを読み込む
gapminder = px.data.gapminder()
# 横に2つのコンポーネントを並べるためのスタイル
half_style = {"width": "50%", "display": "inline-block"}

app = dash.Dash(__name__)

# 2つのコンポーネントを持つレイアウト
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="my_button", n_clicks=0),
        html.Div(id="my_div", children=[]),
    ]
)

# ➊ コールバック1
@app.callback(
    Output("my_div", "children"),
    [Input("my_button", "n_clicks")],
    [State("my_div", "children")],
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            html.P(id={"type": "title", "index": n_clicks}),
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks],
            ),
            dcc.Dropdown(
                id={"type": "my_dropdown2", "index": n_clicks},
                options=[
                    {"label": col, "value": col} for col in gapminder.columns[3:6]
                ],
                value="lifeExp",
            ),
            dcc.Graph(id={"type": "my_graph", "index": n_clicks}),
        ],
        style=half_style,
    )  # 横に2つのレイアウトを並べるためstyleを渡す
    children.append(new_layout)
    return children


# ➋コールバック2
@app.callback(
    [
        Output({"type": "my_graph", "index": MATCH}, "figure"),
        Output({"type": "title", "index": MATCH}, "children"),
    ],
    [
        Input({"type": "my_dropdown", "index": MATCH}, "value"),
        Input({"type": "my_dropdown2", "index": MATCH}, "value"),
    ],  # ➌ indexにMATCHを渡す
)
def update_graph(selected_value, selected_col):
    gap = gapminder[gapminder["country"] == selected_value]
    return px.line(gap, x="year", y=selected_col), str(selected_value)


app.run_server(debug=True)
