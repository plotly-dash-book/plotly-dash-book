import dash
import dash_core_components as dcc

app = dash.Dash(__name__)
app.layout = dcc.Dropdown(
    options=[  # ➊ 選択肢の設定
        {"label": "赤", "value": "赤"},
        {"label": "黄", "value": "黄"},
        {"label": "青", "value": "青"},
    ],
    value="赤",  # ➊ 初期値の設定
    clearable=False,  # ➊ 選択を削除できないように設定
    style={"textAlign": "center"},  # ➊ 文字を中央に寄せる
)
app.run_server(debug=True)
