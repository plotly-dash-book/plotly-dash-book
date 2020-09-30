import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# データの読み込み
tips = px.data.tips()

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

# ➊ レイアウトの作成
app.layout = html.Div(
    [
        # ➌ 指定したグラフに応じてグラフのタイトルを変更
        html.H3(id="title", style={"textAlign": "center"}),
        html.Div(
            [
                html.Div(
                    [
                        html.H4("曜日選択"),
                        # ➍ 曜日選択のドロップダウンの作成
                        dcc.Dropdown(
                            id="day_selector",
                            options=[
                                {"value": dow, "label": dow}
                                for dow in tips.day.unique()
                            ],
                            multi=True,
                            value=["Thur", "Fri", "Sat", "Sun"],
                        ),
                    ],
                    className="six columns",
                ),
                html.Div(
                    [
                        html.H4("グラフ選択"),
                        # ➎ グラフ選択のドロップダウンの作成
                        dcc.Dropdown(
                            id="graph_selector",
                            options=[
                                {"value": "bar", "label": "bar"},
                                {"value": "scatter", "label": "scatter"},
                            ],
                            value="bar",
                        ),
                    ],
                    className="six columns",
                ),
            ],
            style={"padding": "2%", "margin": "auto"},
        ),
        # ➏ グラフの表示場所
        html.Div(
            [
                dcc.Graph(id="app_graph", style={"padding": "3%"}),
            ],
            style={"padding": "3%", "marginTop": 50},
        ),
    ]
)

# ➋ コールバックの作成
@app.callback(
    # ➐ Outputインスタンス,Inputインスタンスの順に配置
    Output("title", "children"),
    Output("app_graph", "figure"),
    Input("day_selector", "value"),
    Input("graph_selector", "value"),
)
def update_graph(selected_days, selected_graph):
    # ➑ データフレームの作成
    selected_df = tips[tips["day"].isin(selected_days)]
    # ➒ 選択されたグラフの種類により、タイトル表示データとグラフを作成
    if selected_graph == "scatter":
        title = "テーブル毎データ（散布図）"
        figure = px.scatter(
            selected_df, x="total_bill", y="tip", color="smoker", height=600
        )
    else:
        title = ("曜日ごとの売り上げ（棒グラフ）",)
        figure = px.bar(selected_df, x="day", y="total_bill", height=600)
    return title, figure


if __name__ == "__main__":
    app.run_server(debug=True)
