import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    # ➊ 各スタイルを設定
    style={
        "width": "500px",  # 横幅: 500px
        "height": "250px",  # 高さ: 250px
        "backgroundColor": "lime",  # 背景色: ライム
        "margin": "50px auto 50px",  # 要素の外側の余白領域 上下50px、autoで中央寄せ
    }
)
if __name__ == "__main__":
    app.run_server(debug=True)
