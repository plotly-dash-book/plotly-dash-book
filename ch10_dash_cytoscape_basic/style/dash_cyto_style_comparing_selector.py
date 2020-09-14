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
        {"data": {"id": "A", "label": "Top Node A"}},
        {"data": {"id": "B", "label": "Node B"}},
        {"data": {"id": "C", "label": "Node C"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B", "weight": 19}},
        {"data": {"source": "B", "target": "C", "weight": 20}},
        {"data": {"source": "C", "target": "A", "weight": 21}},
    ],
    # スタイルの指定
    stylesheet=[  # ノード・エッジ全体に対する指定
        # データ辞書のlabelをラベルとして表示
        {"selector": "node", "style": {"content": "data(label)"}},
        # データ辞書のweightをラベルとして表示
        {"selector": "edge", "style": {"content": "data(weight)"}},
        # データ条件による適用範囲の指定
        # ❶ labelが'Top'から始まるラベルを赤くする
        {"selector": "[label ^= 'Top']", "style": {"color": "red"}},
        # ❷ weightが20以上のエッジを水色の太線にする
        {"selector": "[weight >= 20]", "style": {"width": 10, "line-color": "skyblue"}},
    ],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
