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
    id="node-id-input-compo",
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

# 要素の状態を変更するコールバック関数
@app.callback(
    Output("cyto-compo", "elements"),  # ❶ ネットワーク図のelementsに出力する
    [Input("node-id-input-compo", "value")],  # 入力ボックスの値を受け取る
)
def update_selected_node(node_id):
    # ❷ 新しい要素辞書のリストを作成
    # 指定したIDのノードは選択状態かつ移動不可、それ以外のノードは非選択状態で移動可能
    new_nodes = [
        {"data": {"id": x}, "selected": True, "grabbable": False}
        if x == node_id
        else {"data": {"id": x}, "selected": False, "grabbable": True}
        for x in range(0, 10)
    ]
    new_elements = new_nodes + default_edges

    return new_elements


if __name__ == "__main__":
    app.run_server(debug=True)
