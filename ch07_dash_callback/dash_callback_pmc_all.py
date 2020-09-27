import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL
import plotly.express as px

# gapminderデータを読み込む
gapminder = px.data.gapminder()

app = dash.Dash(__name__)

# レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="my_button"),  # 新たなレイアウトを追加するボタン
        html.Div(id="my_div", children=[]),  # ドロップダウンを追加するDiv
        html.Div(id="my_select"),  # 作成したグラフを描画するDiv
    ]
)

# ➊ コールバック1
@app.callback(
    Output("my_div", "children"),
    [Input("my_button", "n_clicks")],
    [State("my_div", "children")],
    prevent_initial_call=True,  # ➌
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks],
            )
        ]
    )
    children.append(new_layout)
    return children


# ➋ コールバック2
@app.callback(
    Output("my_select", "children"),
    [Input({"type": "my_dropdown", "index": ALL}, "value")],  # ➍
    prevent_initial_call=True,
)
def update_graph(selected_values):
    selected_countries = gapminder[gapminder["country"].isin(selected_values)]  # ➎

    return dcc.Graph(
        figure=px.line(selected_countries, x="year", y="lifeExp", color="country")
    )  # ➏


app.run_server(debug=True)
