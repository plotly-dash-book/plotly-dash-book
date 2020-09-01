import dash
import dash_html_components as html

# ➊ 1段目用CSS辞書
div_style3 = {"height": "250px", "margin": "5%", "backgroundColor": "lime"}

# ➋ 2段目用CSS辞書
div_style4 = {"height": "250px", "backgroundColor": "skyblue"}

# ➌ スタイルシートの読み込み
external_sheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_sheet)

app.layout = html.Div(
    [
        html.H1("5つの長方形を並べたアプリケーション"),
        # ➍ 1段目　2つの長方形
        html.Div(
            [
                html.Div(style=div_style3, className="five columns"),
                html.Div(style=div_style3, className="five columns"),
            ],
            id="first_leader",
        ),
        # ➎ 2段目　3つの長方形
        html.Div(
            [
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
