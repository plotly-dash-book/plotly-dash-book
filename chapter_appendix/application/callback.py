from app import app  # ➊ app.pyから変数 app をインポート
from dash.dependencies import Input, Output


@app.callback(Output("h_one", "style"), [Input("h_one", "n_clicks")])
def upgrade_bcolor(n_clicks):
    if n_clicks % 2 == 0:
        return {"backgroundColor": "yellow"}
    else:
        return {"backgroundColor": "black"}
