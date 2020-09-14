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
        {"data": {"id": "A", "label": "Node A"}},
        {"data": {"id": "B", "label": "Node B"}},
        {"data": {"id": "C", "label": "Node C"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B", "route_name": "A - B"}},
        {"data": {"source": "B", "target": "C", "route_name": "B - C"}},
        {"data": {"source": "C", "target": "A", "route_name": "C - A"}},
    ],
    # ❶ スタイルの指定（リスト形式で複数指定可）
    stylesheet=[  # ノード全体に対するスタイル
        {  # ❷ 適用対象をノードに指定（セレクタ文字列）
            "selector": "node",
            # ❸ 具体的なスタイルを記述
            "style": {
                "content": "data(label)",
                "background-color": "skyblue",
                "shape": "triangle",
            },
        },
        # エッジ全体に対するスタイル
        {  # ❷ 適用対象をエッジに指定（セレクタ文字列）
            "selector": "edge",
            # ❸ 具体的なスタイルを記述（スタイル辞書）
            "style": {"content": "data(route_name)", "line-color": "#f9df9d"},
        },
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
