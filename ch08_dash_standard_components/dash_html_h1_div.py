import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("京都へようこそ！"),
        html.H2("おすすめ観光スポット"),
        html.P("- 清水寺", n_clicks=0, id="one"),
        html.P("- 八坂神社", n_clicks=0, id="two"),
        html.P("- 銀閣寺", n_clicks=0, id="three"),
        html.P("- 大文字", n_clicks=0, id="four"),
        html.P("- 鴨川", n_clicks=0, id="five"),
    ],
    style={"textAlign": "center"},
)

# ➊ ID名のリストからコールバックを作成
for id_ in ["one", "two", "three", "four", "five"]:

    @app.callback(Output(id_, "hidden"), Input(id_, "n_clicks"))
    def letter_disappear(n_clicks):
        if n_clicks % 2 == 1:
            return True


if __name__ == "__main__":
    app.run_server(debug=True)
