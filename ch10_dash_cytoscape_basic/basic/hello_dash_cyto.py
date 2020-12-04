import dash
import dash_cytoscape as cyto
import dash_html_components as html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# ❶ Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="hello-dash-cyto",
    style={"width": "400px", "height": "400px"},
    # ❷ ネットワークの構成要素の定義
    elements=[
        # ❸ ノードの定義
        {"data": {"id": "A"}},
        {"data": {"id": "B"}},
        # ❹ エッジの定義
        {"data": {"source": "A", "target": "B", "label": "A - B"}},
    ],
    # ❺ ノード配置方法の定義
    layout={"name": "grid"},
    # ❻ スタイルの定義
    stylesheet=[
        # ❼ ノード全体に対するスタイル指定（グループセレクタ）
        {"selector": "node", "style": {"content": "data(id)"}},
        # ❽ ノードBに対するスタイル指定
        {"selector": "#B", "style": {"background-color": "red"}},
    ],
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
