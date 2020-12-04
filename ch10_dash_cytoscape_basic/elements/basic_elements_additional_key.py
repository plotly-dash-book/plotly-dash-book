import dash
import dash_cytoscape as cyto
import dash_html_components as html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# ネットワークの構成要素の定義
elements = [
    # ノードの定義に部活動の情報を追加
    {
        "data": {"id": "A", "label": "Alice", "club": "科学部"},
        "position": {"x": 0, "y": -100},
    },
    {
        "data": {"id": "B", "label": "Bob", "club": "科学部"},
        "position": {"x": -100, "y": 0},
    },
    {
        "data": {"id": "C", "label": "Carol", "club": "ボクシング部"},
        "position": {"x": 100, "y": 0},
    },
    {
        "data": {"id": "D", "label": "David", "club": "美術部"},
        "position": {"x": 100, "y": 100},
    },
    # エッジの定義に重みの情報を追加
    {"data": {"source": "A", "target": "B", "weight": 3}},
    {"data": {"source": "A", "target": "C", "weight": 10}},
    {"data": {"source": "C", "target": "D", "weight": 5}},
]

# Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="basic_elements",
    style={"width": "600px", "height": "600px", "padding": "50px"},
    # ネットワークの構成要素の定義
    elements=elements,
    # ノード配置方法の定義
    layout={"name": "preset"},
    # スタイルの指定
    stylesheet=[
        # ノードのスタイル設定
        {"selector": "node", "style": {"content": "data(label)"}},
        # エッジのスタイル設定
        {
            "selector": "edge",
            "style": {
                "content": "data(weight)",
                "width": "data(weight)",
                "opacity": "mapData(weight, 0, 10, 0.3, 1)",
            },
        },
        {"selector": "[club = '科学部']", "style": {"background-color": "skyblue"}},
        {
            "selector": "[club = 'ボクシング部']",
            "style": {"background-color": "sandybrown", "shape": "triangle"},
        },
        {
            "selector": "[club = '美術部']",
            "style": {"background-color": "forestgreen", "shape": "rectangle"},
        },
    ],
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
