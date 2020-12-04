import dash
import dash_cytoscape as cyto
import dash_html_components as html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# ネットワークの構成要素の定義
elements = [
    # ノードの定義
    {
        "data": {"id": "A", "label": "Alice"},
        "position": {"x": 0, "y": -100},
        # ❶ 初期状態で選択した状態に設定
        "selected": True,
    },
    {
        "data": {"id": "B", "label": "Bob"},
        "position": {"x": -100, "y": 0},
        # ❷ 選択不可に設定
        "selectable": False,
    },
    {
        "data": {"id": "C", "label": "Carol"},
        "position": {"x": 100, "y": 0},
        # ❸ 位置を固定に設定
        "locked": True,
    },
    {
        "data": {"id": "D", "label": "David"},
        "position": {"x": 100, "y": 100},
        # ❹ ドラッグ&ドロップによる移動不可に設定
        "grabbable": False,
    },
    # エッジの定義
    {"data": {"source": "A", "target": "B"}},
    {"data": {"source": "A", "target": "C"}},
    {"data": {"source": "C", "target": "D"}},
]

# Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="basic_elements",
    style={"width": "600px", "height": "600px", "padding": "50px"},
    # ネットワークの構成要素の定義
    elements=elements,
    # ノード配置方法の定義
    layout={"name": "preset"},
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
