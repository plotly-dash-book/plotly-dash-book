import json

import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

# Dashインスタンスの生成
app = dash.Dash(__name__)

# ネットワークの構成要素の定義
elements = [
    # ノードの定義
    {"data": {"id": "A", "name": "Alice", "age": 14},},
    {"data": {"id": "B", "name": "Bob", "age": 13},},
    {"data": {"id": "C", "name": "Carol", "age": 13},},
    {"data": {"id": "D", "name": "David", "age": 14},},
    # エッジの定義
    {"data": {"id": "AB", "source": "A", "target": "B", "weight": 3}},
    {"data": {"id": "AC", "source": "A", "target": "C", "weight": 10}},
    {"data": {"id": "CD", "source": "C", "target": "D", "weight": 5}},
]

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

cyto_compo = cyto.Cytoscape(
    id="cyto-compo",
    style={"width": "400px", "height": "400px"},
    layout={"name": "breadthfirst", "roots": "#A", "animate": True},
    elements=elements,
    stylesheet=default_stylesheet,
)

# クリックしたノードの情報を表示する<p>タグ
pre_compo = html.Pre(
    id="pre-compo", style={"backgroundColor": "#CCCCCC", "fontSize": "20px"}
)

app.layout = html.Div([pre_compo, cyto_compo])


def get_neighbor_node_ids(node_element_dict):  # ❶
    """
    ノードの要素辞書から隣接ノードのIDのリストを取得する
    """
    # クリックしたノードのID
    node_id = node_element_dict["data"]["id"]
    # 隣接ノードのIDを取得する
    neighbor_node_ids = [x["source"] for x in node_element_dict["edgesData"]]
    neighbor_node_ids += [x["target"] for x in node_element_dict["edgesData"]]
    # 自分自身のノードIDは除外する
    neighbor_node_ids = list(set(neighbor_node_ids) - set(node_id))
    return neighbor_node_ids


# ❷ クリックしたノードの隣接ノードのスタイルを変更するコールバック関数
@app.callback(
    Output("cyto-compo", "stylesheet"),  # スタイル設定を変化させる
    [Input("cyto-compo", "tapNode")],  # クリックしたノードの要素辞書全体を受け取る
)
def change_neighbor_node_style(node_element_dict):
    if not node_element_dict:
        return default_stylesheet

    # 隣接ノードのIDのリストを取得
    neighbor_node_ids = get_neighbor_node_ids(node_element_dict)

    # 隣接ノードのスタイルを作成する
    new_styles = []

    for node_id in neighbor_node_ids:
        # 隣接ノードの背景色は赤
        style = {"selector": f"#{node_id}", "style": {"background-color": "red"}}
        new_styles.append(style)

    new_stylesheet = default_stylesheet + new_styles

    return new_stylesheet


if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
