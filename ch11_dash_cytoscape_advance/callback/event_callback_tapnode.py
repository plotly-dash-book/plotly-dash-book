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

# クリックしたノードのデータ辞書を表示するコールバック関数
@app.callback(
    Output("pre-compo", "children"),
    [Input("cyto-compo", "tapNode")],  # ❶ クリックしたノードの要素辞書全体を受け取る
)
def show_tapped_node(node_element_dict):
    if not node_element_dict:
        return "ノードをクリックしてください"
    # ❷ 受け取ったノードの要素辞書全体を整形して返す
    return json.dumps(node_element_dict, indent=2)


if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
