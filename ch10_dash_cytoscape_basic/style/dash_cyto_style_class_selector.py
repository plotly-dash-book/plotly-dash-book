import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

cyto_compo = cyto.Cytoscape(
    id="dash-cyto-styling",
    style={"width": "500px", "height": "400px"},
    # ノード配置方法の定義
    layout={"name": "circle"},
    # ネットワーク構造を構成する要素の定義
    elements=[
        # ノードの定義（各ノードに対し"rect", "green"のクラスを指定）
        {"data": {"id": "A", "label": "A (plain)"}},  # クラス指定なし
        {"data": {"id": "B", "label": "B (rect)"}, "classes": "rect"},  # ❶ クラスを1つ指定
        {"data": {"id": "C", "label": "C (green)"}, "classes": "green"},  # ❶ クラスを1つ指定
        {
            "data": {"id": "D", "label": "D (rect & green)"},
            "classes": "rect green",  # ❷ クラスを複数指定
        },
        # エッジの定義（各ノードに対し"bold", "curve"のクラスを指定）
        {"data": {"source": "A", "target": "B", "label": "plain"}},  # クラス指定なし
        {
            "data": {"source": "B", "target": "C", "label": "Bold"},
            "classes": "bold",  # ❶ クラスを1つ指定
        },
        {
            "data": {"source": "C", "target": "D", "label": "Curve"},
            "classes": "curve",  # ❶ クラスを1つ指定
        },
        {
            "data": {"source": "D", "target": "A", "label": "Bold & Curve"},
            "classes": "bold curve",  # ❷ クラスを複数指定
        },
    ],
    # スタイルの指定
    stylesheet=[
        {"selector": "node", "style": {"content": "data(label)"}},
        {"selector": "edge", "style": {"content": "data(label)"}},
        # ❸ クラス・セレクタによる指定
        {"selector": ".rect", "style": {"shape": "rectangle"}},
        {"selector": ".green", "style": {"background-color": "green"}},
        {"selector": ".bold", "style": {"width": 10}},
        {"selector": ".curve", "style": {"curve-style": "segments"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
