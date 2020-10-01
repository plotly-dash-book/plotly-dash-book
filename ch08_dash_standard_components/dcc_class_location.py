import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # Locationコンポーネントの設置
        dcc.Location(id="my_location"),
        # コールバックの出力先となる4つのDivクラス
        html.Div(id="show_location1", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location2", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location3", style={"fontSize": 30, "textAlign": "center"}),
        html.Div(id="show_location4", style={"fontSize": 30, "textAlign": "center"}),
        # Linkコンポーネントの設置
        html.Br(),
        dcc.Link("/test", href="/test"),
        html.Br(),
        dcc.Link("/test?what", href="/test?what"),
        html.Br(),
        dcc.Link("/test?what#dashhash", href="/test?what#dashhash"),
        html.Br(),
        dcc.Link("home", href="/"),
    ],
    style={"fontSize": 30, "textAlign": "center"},
)

# ➊ URLを4つの ``Div`` クラスに返すコールバック
@app.callback(
    Output("show_location1", "children"),
    Output("show_location2", "children"),
    Output("show_location3", "children"),
    Output("show_location4", "children"),
    Input("my_location", "href"),
    Input("my_location", "pathname"),
    Input("my_location", "search"),
    Input("my_location", "hash"),
)
def update_location(url, pathname, search, hash):
    return (
        f"href={url}",
        f"pathname={pathname}",
        f"search={search}",
        f"hash={hash}",
    )


if __name__ == "__main__":
    app.run_server(debug=True)
