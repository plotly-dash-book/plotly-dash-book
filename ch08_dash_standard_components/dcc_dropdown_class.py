import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # ➊ ドロップダウンを作成
        dcc.Dropdown(
            # ➋ 選択肢の定義。"label"と"value"が必須
            options=[
                {"label": "東京", "value": "tokyo"},
                {"label": "北海道", "value": "hokkaido"},
                {"label": "静岡", "value": "shizuoka"},
                {"label": "愛知", "value": "aichi"},
                {"label": "京都", "value": "kyoto"},
            ],
            # ➌ 初期値を京都に設定
            value="kyoto",
            # ➍ 文字を真ん中に寄せる
            style={"textAlign": "center"},
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
