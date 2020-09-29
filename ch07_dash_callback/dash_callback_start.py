import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ➊ レイアウト 各コンポーネントにIDを付ける
app.layout = html.Div(
    [
        # コールバックの返り値を表示する
        html.H1(id="head-title"),
        # 文字を入力するテキストエリア
        dcc.Textarea(
            id="my-text-state",
            value="initial value",  # 初期値の設定
            style={"width": "80%", "fontSize": 30},
        ),
        # クリックするとコールバックを呼び出すボタン
        html.Button(id="my-button", n_clicks=0, children="submit"),
    ],
    style={"margin": 50},
)

# ➋ コールバックの作成。
@app.callback(
    Output("head-title", "children"),  # ➌ 出力項目
    Input("my-button", "n_clicks"),  # ➍ 入力項目
    State("my-text-state", "value"),  # ➎ 状態項目
)
# ➏ コールバック関数
def update_title(n_clicks, text_value):
    return text_value


if __name__ == "__main__":
    app.run_server(debug=True)
