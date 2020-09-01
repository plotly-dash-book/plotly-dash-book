import dash
import dash_core_components as dcc
import dash_html_components as html

# 外部スタイルシートの読み込み
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        # ➊ 各コンポーネントへのスタイルシートの適用
        html.H1("スタイル", className="three columns"),
        dcc.Input(placeholder="スタイルシートテスト", className="three columns"),
        dcc.Graph(className="six columns"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
