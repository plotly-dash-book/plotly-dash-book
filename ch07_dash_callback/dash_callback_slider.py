import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ➊ レイアウト
app.layout = html.Div(
    [
        html.H1(id="callback-output"),
        # 引数updatemodeに"drag"を渡し,動作を即座に反映するように設定
        dcc.Slider(id="callback-input", value=0, updatemode="drag"),
    ],
    style={"textAlign": "center", "width": "60%", "margin": "auto"},
)

# ➋ コールバック
@app.callback(
    # ➌ 出力項目を指定,ID,属性を渡す
    Output("callback-output", "children"),
    # ➍ 入力項目を指定,ID,属性を渡す
    Input("callback-input", "value"),
)
# ➎ コールバック関数
def update_app(num_value):
    return num_value


if __name__ == "__main__":
    app.run_server(debug=True)
