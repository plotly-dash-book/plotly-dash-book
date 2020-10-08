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
        {"data": {"id": "A", "color": "red"}},
        {"data": {"id": "B", "color": "yellow"}},
        {"data": {"id": "C", "color": "blue"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B"}},
        {"data": {"source": "B", "target": "C"}},
        {"data": {"source": "C", "target": "A"}},
    ],
    # スタイルの指定
    stylesheet=[
        #
        {
            "selector": "node",
            "style": {
                "background-opacity": 0.6,  # ❶ 固定値で背景の不透明度を指定
                "background-color": "data(color)",  # ❷ データ辞書の値を使って指定
            },
        },
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
