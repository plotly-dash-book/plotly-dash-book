import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

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

# ❶ 削除ボタンを追加
button = html.Button(id="remove-button-compo", n_clicks=0, children="remove")

app.layout = html.Div([node_id_input, button, cyto_compo])

# 指定したノードを削除するコールバック関数
@app.callback(
    Output("cyto-compo", "elements"),  # ネットワーク図のelementsに出力する
    [Input("remove-button-compo", "n_clicks"),],  # ❷ トリガーとなるボタンを指定
    [
        State("node-id-input-compo", "value"),  # ❸ 入力ボックスの値を受け取る
        State("cyto-compo", "elements"),  # ❹ ネットワークの構成要素の値を受け取る
    ],
)
def update_selected_node(n_clicks, node_id, current_elements):
    if n_clicks < 1:
        # 画面リロード時にコールバック関数が実行されたときは何もしない
        return current_elements

    # ❺ 新しい要素辞書のリストの作成
    # 現在のネットワークの構成要素から、指定されたノードを取り除く
    # 指定されたノードを始点または終点に持つエッジも取り除く
    new_elements = []

    for element in current_elements:
        # 指定されていないノードだけを残す
        if "id" in element["data"]:
            if element["data"]["id"] != node_id:
                new_elements.append(element)

        # 指定されたノードと関係ないエッジだけを残す
        if "source" in element["data"]:
            if (element["data"]["source"] != node_id) and (
                element["data"]["target"] != node_id
            ):
                new_elements.append(element)

    return new_elements


if __name__ == "__main__":
    app.run_server(debug=True)
