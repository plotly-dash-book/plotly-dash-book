import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ➊ レイアウト
app.layout = html.Div(
    [
        html.H1(id="callback-output"),
        # valueに初期値0を設定
        dcc.Slider(id="callback-input", value=0),
    ],
    style={"textAlign": "center", "width":"60%", "margin": "auto"},
)

# ➋ コールバック
@app.callback(
    # ➌ コールバック関数の戻り値の出力先を指定
    Output("callback-output", "children"),
    # ➍ コールバック関数を呼び出すコンポーネント属性の指定
    [Input("callback-input", "value")],
)
# ➎ コールバック関数
def update_app(num_value):
    return num_value


if __name__ == "__main__":
    app.run_server(debug=True)
