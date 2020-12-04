import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ノードを10個定義
default_nodes = [{"data": {"id": x}} for x in range(10)]

# エッジを定義 (木構造)
default_edges = [
    {"data": {"source": 0, "target": 1}},
    {"data": {"source": 0, "target": 2}},
    {"data": {"source": 0, "target": 3}},
    {"data": {"source": 1, "target": 4}},
    {"data": {"source": 1, "target": 5}},
    {"data": {"source": 2, "target": 6}},
    {"data": {"source": 2, "target": 7}},
    {"data": {"source": 3, "target": 8}},
    {"data": {"source": 3, "target": 9}},
]

elements = default_nodes + default_edges

# ノードIDを入力するボックス
node_id_input = dcc.Input(
    style={"fontSize": "25px"},
    id="input-compo",
    placeholder=0,
    type="number",
    value=0,
    max=9,
    min=0,
)

# デフォルトのスタイルシート
default_stylesheet = [
    {"selector": "node", "style": {"content": "data(id)", "font-size": "25px",},},
    {
        "selector": "edge",
        "style": {
            "mid-target-arrow-shape": "vee",
            "line-color": "skyblue",
            "mid-target-arrow-color": "skyblue",
            "arrow-scale": 3,
        },
    },
]

# ネットワーク図の用意
cyto_compo = cyto.Cytoscape(
    id="cyto-compo",
    layout={"name": "breadthfirst", "roots": "#0", "animate": True},
    style={"width": "400px", "height": "400px"},
    elements=elements,
    stylesheet=default_stylesheet,
)

app.layout = html.Div([node_id_input, cyto_compo])

# スタイルシートを変更するコールバック関数
@app.callback(
    Output("cyto-compo", "stylesheet"),  # ❶ ネットワーク図のstylesheetに出力する
    [Input("input-compo", "value")],  # 入力ボックスの値を受け取る
)
def update_style(node_id):
    # ❷ 入力したノードID用のスタイル
    new_style = {"selector": f"#{node_id}", "style": {"background-color": "red"}}

    # ❸ デフォルトのスタイルに新しいスタイルを追加する
    # ※ default_stylesheetはグローバル変数なので、コールバック関数内で変更しないこと
    new_stylesheet = default_stylesheet + [new_style]

    return new_stylesheet


if __name__ == "__main__":
    app.run_server(debug=True)
