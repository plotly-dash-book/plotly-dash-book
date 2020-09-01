import dash
import dash_core_components as dcc
import dash_html_components as html

# タブが選択された際のスタイル（Tabコンポーネントに渡す）
tab_selected_style = {
    "backgroundColor": "limegreen",
    "color": "white",
    "fontWeight": "bold",
}

app = dash.Dash(__name__)

bc_color = {"backgroundColor": "#D7FFF1"}

app.layout = html.Div(
    [
        html.H1("Plotly-Dash-Book"),
        # ➊ タブ全体を管理するTabsコンポーネント
        dcc.Tabs(
            id="tabs",
            value="index",  # ➋ 起動時に表示するページの ``value`` を設定
            # ➌ children属性に4つのTabコンポーネントを格納する
            children=[
                dcc.Tab(
                    label="index-Page",  # ➍ タブに表示される値
                    value="index",  # ➎ 選択された際の値
                    selected_style=tab_selected_style,  # 選択された際のスタイル
                    children=[html.Div(html.H2("index-Page"))],  # ➏ コンテンツ
                ),
                dcc.Tab(
                    label="Plotly-Page",
                    value="plotly",
                    selected_style=tab_selected_style,
                    children=[html.Div([html.H2("Plotly-Page")])],
                ),
                dcc.Tab(
                    label="Dash-Page",
                    value="dash",
                    selected_style=tab_selected_style,
                    children=[html.Div([html.H2("Dash-Page")])],
                ),
                dcc.Tab(
                    label="Cytoscape-Page",
                    value="cytoscape",
                    selected_style=tab_selected_style,
                    children=[html.Div([html.H2("Cytoscape-Page")])],
                ),
            ],
        ),
        html.H1("For data analysis"),  # ➓ タブ下のタイトル
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
