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
    # スタイルの指定（リスト形式で複数指定可）
    stylesheet=[  # ❶ ノード全体に対する指定
        {  # ❹ 適用対象を指定（セレクタ文字列）
            "selector": "node",
            # ❺ 具体的なスタイルを記述（スタイル辞書）
            "style": {
                "content": "data(label)",
                "background-color": "skyblue",
                "shape": "triangle",
            },
        },
        # ❷ エッジ全体に対する指定
        {  # ❹ 適用対象を指定（セレクタ文字列）
            "selector": "edge",
            # ❺ 具体的なスタイルを記述（スタイル辞書）
            "style": {"content": "data(route_name)", "line-color": "#f9df9d"},
        },
        # ❸ 特定のノードに対する指定
        {  # ❹ 適用対象を指定（セレクタ文字列）
            "selector": "#C",  # IDがCのノード
            # ❺ 具体的なスタイルを記述（スタイル辞書）
            "style": {"border-width": 5, "border-color": "red"},
        },
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
