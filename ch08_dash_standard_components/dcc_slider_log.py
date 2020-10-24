import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Slider(
            id="thisSlider",
            max=5,  # 最大値
            value=2,  # 初期値
            step=0.01,  # 最小目盛のステップ
            tooltip={"always_visible": False, "placement": "bottom"},  # ツールチップを下側に表示
            updatemode="drag",  # ➊ ハンドルへのスライダの反応
        ),
        html.P(
            id="pow-output", style={"marginTop": "5%", "fontSize": 30}
        ),  # コールバックの返り値を受け取る
    ],
    style={"width": "80%", "margin": "5% auto"},
)

# ➋ コールバック
@app.callback(
    dash.dependencies.Output("pow-output", "children"),
    [dash.dependencies.Input("thisSlider", "value")],
)
def display_value(value):
    return f"数値: {value} | 10のべき乗: {10 ** value: .3f}"


if __name__ == "__main__":
    app.run_server(debug=True)
