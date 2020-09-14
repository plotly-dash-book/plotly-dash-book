import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

# ノードを10個定義
nodes = [{"data": {"id": x, "label": f"{x}"}} for x in range(0, 10)]

# エッジを定義 (木構造)
edges = [
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

elements = nodes + edges

cyto_compo = cyto.Cytoscape(
    id="dash_cyto_layout",
    style={"width": "400px", "height": "400px"},
    layout={"name": "breadthfirst", "roots": "#0", "circle": True},  # ❶サークルモードを指定
    elements=elements,
    stylesheet=[
        {"selector": "node", "style": {"content": "data(label)"}},
        {
            "selector": "edge",
            "style": {"mid-target-arrow-shape": "vee", "arrow-scale": 3},
        },
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
