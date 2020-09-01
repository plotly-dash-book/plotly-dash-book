import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    # スタイルの設定
    style={
        "fontSize": 50,  # フォントサイズ
        "color": "white",  # 文字色
        "backgroundColor": "#000000",  # 背景色
        "width": 400,  # 横幅
        "margin": "auto",  # ➊ コンポーネントを中央に寄せる
    },
)

if __name__ == "__main__":
    app.run_server(debug=True)
