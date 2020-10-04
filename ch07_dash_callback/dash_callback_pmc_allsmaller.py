import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL, ALLSMALLER, MATCH
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

# コールバック1
@app.callback(
    Output("my_div", "children"),
    Input("my_button", "n_clicks"),
    State("my_div", "children"),
    prevent_initial_call=True,
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
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


# コールバック2
@app.callback(
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    # ➊ 1つ目のInputのindexにALLSMALLER,2つ目,3つ目にMATCHを渡す
    Input({"type": "my_dropdown", "index": ALLSMALLER}, "value"),
    Input({"type": "my_dropdown", "index": MATCH}, "value"),  # ➋
    Input({"type": "my_dropdown2", "index": MATCH}, "value"),
)
def update_graph(allsmaller_value, matching_value, selected_col):
    selected_value = allsmaller_value + [matching_value]  # ➌
    selected_countries = gapminder[gapminder["country"].isin(selected_value)]  # ➍
    return px.line(selected_countries, x="year", y=selected_col, color="country")  # ➎


app.run_server(debug=True)
