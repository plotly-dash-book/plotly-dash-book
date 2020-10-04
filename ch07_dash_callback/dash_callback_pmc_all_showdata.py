import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL
import plotly.express as px

# gapminderデータを読み込む
gapminder = px.data.gapminder()

app = dash.Dash(__name__)

# ➊ レイアウトの作成
app.layout = html.Div(
    [
        html.Button("PUSH ME", id="add_drop"),  # 新たなドロップダウンを追加するボタン（➋）
        html.Div(id="show_drop", children=[]),  # ドロップダウンを追加するDiv（➌）
        html.P(id="my_text"),  # テキストを描画するP（➍）
    ],
    style={"width": "80%", "margin": "2% auto"},
)

# ➎ コールバック1
@app.callback(
    Output("show_drop", "children"),
    Input("add_drop", "n_clicks"),
    State("show_drop", "children"),
    prevent_initial_call=True,  # ➏
)
def update_layout(n_clicks, children):
    new_layout = html.Div(
        [
            dcc.Dropdown(
                id={"type": "my_dropdown", "index": n_clicks},  # ➐
                options=[{"label": c, "value": c} for c in gapminder.country.unique()],
                value=gapminder.country.unique()[n_clicks - 1],
            )
        ]
    )
    children.append(new_layout)  # ➑
    return children


# ➒ コールバック2
@app.callback(
    Output("my_text", "children"),
    Input({"type": "my_dropdown", "index": ALL}, "value"),  # ➓
    prevent_initial_call=True,
)
def update_graph(selected_values):
    # 全てのドロップダウンで選択された国のリストを文字列にする
    return str(selected_values)


app.run_server(debug=True)
