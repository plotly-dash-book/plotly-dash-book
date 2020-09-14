import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

# ノードの定義
nodes = [
    # ❶ 各ノードの位置を個別に指定
    {"data": {"id": "A", "label": "(0, 0)"}, "position": {"x": 0, "y": 0}},
    {"data": {"id": "B", "label": "(50, 0)"}, "position": {"x": 50, "y": 0},},
    {"data": {"id": "C", "label": "(50, 50)"}, "position": {"x": 50, "y": 50},},
    {"data": {"id": "D", "label": "(0, 100)"}, "position": {"x": 0, "y": 100},},
    {"data": {"id": "E", "label": "(100, 0)"}, "position": {"x": 100, "y": 0}},
]

# エッジの定義
edges = [
    {"data": {"source": "A", "target": "C"}},
    {"data": {"source": "A", "target": "D"}},
    {"data": {"source": "D", "target": "A"}},
    {"data": {"source": "A", "target": "B"}},
    {"data": {"source": "B", "target": "E"}},
]

elements = nodes + edges

cyto_compo = cyto.Cytoscape(
    id="dash_cyto_layout",
    style={"width": "400px", "height": "400px"},
    # ❷ 位置を手動で配置するよう指定
    layout={"name": "preset"},
    elements=elements,
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
