import dash
import dash_cytoscape as cyto
import dash_html_components as html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="hello-dash-cyto",
    style={"width": "400px", "height": "400px"},
    # ネットワークの構成要素の定義
    elements=[
        # ノードの定義
        {"data": {"id": "A", "name": "Alice"}},
        {"data": {"id": "B", "name": "Bob"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B",
                  "name": "family",
                  "source_name": "parent", "target_name": "child"}},
    ],
    # ノード配置方法の定義
    layout={"name": "grid"},
    # スタイルの定義
    stylesheet=[
        # ❶ ノード全体のラベルを変更
        {"selector": "node",
         "style": {"label": "data(name)",  # ラベル文字列
                   "color": "white",  # 文字色を白
                   "text-background-color": "green",  # 背景色を緑
                   "text-background-opacity": 1,  # 完全に不透明
                   "text-halign": "right",  # ノードの右側
                   "text-valign": "center",}}, # ノードの中央
        # ❷ エッジ全体のラベルを変更
        {"selector": "edge",
         "style": {"content": "data(name)",  # ラベル文字列
                   "source-label": "data(source_name)",  # 始点側のラベル文字列
                   "target-label": "data(target_name)",  # 終点側のラベル文字列
                   "source-text-offset": 25,  # 始点側のラベルの位置
                   "target-text-offset": 25}},  # 終点側のラベルの位置
    ],
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
