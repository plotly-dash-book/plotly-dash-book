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

# ルートとなるノードIDを入力するボックス
bfs_roots_input = dcc.Input(
    style={"fontSize": "25px"},
    id="input-compo",
    placeholder=0,
    type="number",
    value=0,
    max=9,
    min=0,
)

# ネットワーク図の用意
cyto_compo = cyto.Cytoscape(
    id="cyto-compo",
    # ❶ 初期状態ではノード0をルートにして階層的に配置する
    layout={"name": "breadthfirst", "roots": "#0", "animate": True},
    style={"width": "400px", "height": "400px"},
    elements=elements,
    stylesheet=[
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
    ],
)

app.layout = html.Div([bfs_roots_input, cyto_compo])

# コールバックの用意
@app.callback(
    Output("cyto-compo", "layout"),  # ❷ ノードの配置を変化させる
    [Input("input-compo", "value")],  # ❸ 入力ボックスの値を受け取る
)
def update_layout(root_node_id):
    # ❹ 新しいレイアウト辞書
    new_layout = {
        "name": "breadthfirst",
        "roots": f"#{root_node_id}",  # 入力されたノードID
        "animate": True,
    }

    return new_layout


if __name__ == "__main__":
    app.run_server(debug=True)
