import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

core_style = {"width": "80%", "margin": "5% auto"}

app = dash.Dash(__name__)

# ➊ レイアウト
app.layout = html.Div(
    [
        html.H1("Hello Dash", style={"textAlign": "center"}),
        dcc.Dropdown(
            # ➌ ID名の追加
            id="my-dropdown",
            options=[
                {"label": "white", "value": "white"},
                {"label": "yellow", "value": "yellow"},
            ],
            value="white",
            style=core_style,
        ),
        dcc.Graph(
            figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
        ),
    ],
    # ➍ ID名の追加
    id="all-components",
)

# ➋ コールバック
@app.callback(
    # ➍ 戻り値の出力先を指定
    Output("all-components", "style"),
    # ➎ コールバックの呼び出し要素の指定
    Input("my-dropdown", "value"),
)
def update_background(selected_value):
    # ➏ 返り値
    return {"backgroundColor": selected_value, "padding": "3%"}


if __name__ == "__main__":
    app.run_server(debug=True)
