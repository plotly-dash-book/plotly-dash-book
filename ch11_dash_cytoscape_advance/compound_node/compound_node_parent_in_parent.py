import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

# 親子関係があるノードを定義
elements = [
    # 親ノードの定義（親ノードを他の親ノードの子にする）
    {"data": {"id": "p_A", "label": "Parent A", "parent": "p_top"}},
    {"data": {"id": "p_B", "label": "Parent B", "parent": "p_top"}},
    {"data": {"id": "p_top", "label": "Top Parent"}},  # 新しい親ノード
    # 子ノードの定義
    {"data": {"id": "c_a", "label": "child a", "parent": "p_A"}},  # ❹
    {"data": {"id": "c_b", "label": "child b", "parent": "p_B"}},  # ❹
    {"data": {"id": "c_c", "label": "child c", "parent": "p_A"}},  # ❹
    {"data": {"id": "c_d", "label": "child d"}},  # ❺ 親なし
    # エッジの定義
    {"data": {"source": "p_A", "target": "p_B"}, "classes": "parents",},  # 親ノード同士
    {"data": {"source": "c_a", "target": "c_b"}, "classes": "children",},  # 子ノード同士
    {"data": {"source": "c_a", "target": "c_c"}, "classes": "children",},  # 子ノード同士
    {
        "data": {"source": "p_A", "target": "c_d"},  # 親と子ノード同士
        "classes": "parents children",
    },
]

cyto_compo = cyto.Cytoscape(
    id="dash_cyto_compound-node",
    layout={"name": "circle"},
    style={"width": "350px", "height": "450px"},
    elements=elements,
    stylesheet=[
        {"selector": "node", "style": {"content": "data(label)"}},
        {"selector": ".parents", "style": {"line-color": "red"}},
        {"selector": ".children", "style": {"line-style": "dashed"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
