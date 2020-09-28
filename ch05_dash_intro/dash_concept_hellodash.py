import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# ➊ コンポーネントのスタイル設定. 横幅80％,中央寄せにし,上下に5％の余白を作る.
core_style = {"width": "80%", "margin": "5% auto"}


app = dash.Dash(__name__)

# ➋ レイアウトにdivの子要素として3つのコンポーネントを渡す
app.layout = html.Div(
    [  # ➌ 見出しを作成する
        html.H1("Hello Dash", style={"textAlign": "center"}),
        # ➍ ドロップダウンを作成する
        dcc.Dropdown(
            options=[
                {"label": "white", "value": "white"},
                {"label": "yellow", "value": "yellow"},
            ],
            value="white",
            style=core_style,
        ),
        # ➎ グラフを作成する
        dcc.Graph(
            figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
