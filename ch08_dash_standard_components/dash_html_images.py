from datetime import datetime

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ボタンを丸く表示するスタイル設定
b_style = {"height": 100, "width": 100, "borderRadius": "50%", "fontSize": 50}

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("ボタンをクリックすると画像が変わります"),
                html.Img(id="bird-img", style={"height": 600}),
            ]
        ),
        html.Button(id="b-one", children="1", style=b_style),
        html.Button(id="b-two", children="2", style=b_style),
        html.Button(id="b-three", children="3", style=b_style),
    ],
    style={"width": "80%", "margin": "auto"},
)

# ➊ コールバック
@app.callback(
    Output("bird-img", "src"),
    Input("b-one", "n_clicks"),
    Input("b-two", "n_clicks"),
    Input("b-three", "n_clicks"),
)
def update_image(c_one, c_two, c_three):
    # ➋ コールバックを呼び出したコンポーネントのID名を渡す
    selected_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    if selected_id == "b-two":
        return "assets/bird2.png"
    elif selected_id == "b-three":
        return "assets/bird3.png"
    else:
        return "assets/bird1.png"


if __name__ == "__main__":
    app.run_server(debug=True)
