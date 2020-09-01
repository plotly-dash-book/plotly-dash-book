import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# ➊ コンポーネントのスタイルの作成
core_style = {"width": "80%", "margin": "5% auto"}


app = dash.Dash(__name__)

# ➋ レイアウトの作成
app.layout = html.Div(
    [  # ➌ Divの子要素に3つのコンポーネントを渡す
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
            figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]),
            style=core_style,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
