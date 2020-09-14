import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

cyto_compo = cyto.Cytoscape(
    id="dash-cyto-styling",
    style={"width": "400px", "height": "400px"},
    # ノード配置方法の定義
    layout={"name": "circle"},
    # ネットワーク構造を構成する要素の定義
    elements=[
        # ノードの定義
        {"data": {"id": "A"}},
        {"data": {"id": "B"}},
        {"data": {"id": "C"}},
        {"data": {"id": "D"}},
        {"data": {"id": "E"}},
        {"data": {"id": "F"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B"}},
        {"data": {"source": "B", "target": "C"}},
        {"data": {"source": "B", "target": "D"}},
        {"data": {"source": "D", "target": "A"}},
        {"data": {"source": "E", "target": "A"}},
        {"data": {"source": "F", "target": "A"}},
    ],
    # スタイルの指定
    stylesheet=[  # ノード・エッジ全体に対する指定
        {"selector": "node", "style": {"content": "data(id)"}},
        # ❶ メタデータによる指定（次数が2より大きいエッジを赤くする）
        {"selector": "[[degree > 2]]", "style": {"background-color": "red"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
