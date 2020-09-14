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
        # ❶ 各ノードにIDを設定する
        {"data": {"id": "A", "label": "Node A"}},
        {"data": {"id": "B", "label": "Node B"}},
        {"data": {"id": "C", "label": "Node C"}},
        # エッジの定義
        # ❷ 各エッジにIDを設定する
        {"data": {"id": "AB", "source": "A", "target": "B", "route_name": "A - B"}},
        {"data": {"id": "BC", "source": "B", "target": "C", "route_name": "B - C"}},
        {"data": {"id": "CA", "source": "C", "target": "A", "route_name": "C - A"}},
    ],
    # スタイルの指定（リスト形式で複数指定可）
    stylesheet=[
        {
            "selector": "#A",  # ❸ id = Aのノードだけにスタイルを適用
            "style": {
                "content": "data(label)",
                "width": 100,
                "height": 100,
                "background-color": "red",
            },
        },
        {
            "selector": "#CA",  # ❸ id = CAのエッジだけにスタイルを適用
            "style": {"content": "data(route_name)", "line-style": "dashed"},
        },
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
