import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P(
            "こんにちは。昨日は雪が降りました。",
            style={
                "fontSize": 50,  # フォントサイズ
                "color": "white",  # 文字色
                "backgroundColor": "#000000",  # 背景色
                "width": "40%",
                "display": "inline-block",  # ➊
            },
        ),
        html.P(
            "こんにちは。今日は晴れました。",
            style={
                "fontSize": 50,  # フォントサイズ
                "color": "white",  # 文字色
                "backgroundColor": "red",  # 背景色
                "width": "40%",
                "display": "inline-block",  # ➊
                "verticalAlign": "top",  # ➋
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
