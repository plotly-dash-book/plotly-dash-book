import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output, State

tips = px.data.tips()

dash_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=dash_stylesheets)

app.layout = html.Div(
    [
        # アプリケーションのタイトル
        html.H1(id="head-title"),
        html.Div(
            [
                # ➊ グラフの種類を選択するDropdownとタイトル
                html.P("グラフの種類の選択"),
                dcc.Dropdown(
                    id="graph-drop",
                    options=[
                        {"value": "bar", "label": "棒グラフ"},
                        {"value": "scatter", "label": "散布図"},
                    ],
                    value="bar",
                ),
                html.Div(
                    # グラフの表示要素を選択するRadioItems
                    [html.P(id="selector-title"), dcc.RadioItems(id="show-selector")]
                ),
            ],
            style={"float": "left", "width": "35%"},
        ),
        html.Div(
            # 選択された種類のグラフを表示するGraph
            [dcc.Graph(id="show-graph")],
            style={"display": "inline-block", "width": "65%", "height": 800},
        ),
    ]
)

# ➋ コールバック1
@app.callback(
    Output("show-selector", "options"),  # RadioItems（id="show-title"）の選択肢
    Output("show-selector", "value"),  # RadioItems（id="show-title"）の値
    Output("head-title", "children"),  # H1（id="head-title"）の表示する文字
    Output("selector-title", "children"),  # P（id="selector-title"）の表示する文字
    Input("graph-drop", "value"),  # Dropdown（id="graph-drop"）で選択された値
)
def update_selector(graph_type):
    if graph_type == "bar":
        return (  # 4つの返り値を作成
            [
                {"value": "total_bill", "label": "総額"},
                {"value": "sex", "label": "性別"},
                {"value": "smoker", "label": "喫煙 / 禁煙"},
                {"value": "time", "label": "時間帯（昼 / 夜）"},
            ],
            "total_bill",
            "チップデータ（棒グラフ）",
            "棒グラフ選択肢",
        )

    return (  # 4つの返り値を作成
        [
            {"value": "smoker", "label": "喫煙 / 禁煙"},
            {"value": "sex", "label": "性別"},
            {"value": "day", "label": "曜日"},
            {"value": "time", "label": "時間帯（昼 / 夜）"},
        ],
        "smoker",
        "チップデータ（散布図）",
        "散布図選択肢",
    )


# ➌ コールバック2
@app.callback(
    Output("show-graph", "figure"),  #
    Input("show-selector", "value"),
    State("graph-drop", "value"),
)
def update_graph(selected_value, graph_type):
    if graph_type == "bar":
        return px.bar(
            tips,
            x="day",
            y="total_bill",
            color=selected_value,
            barmode="group",
            height=600,
            title=f"チップデータ棒グラフ（要素: {selected_value}）",
        )
    else:
        return px.scatter(
            tips,
            x="total_bill",
            y="tip",
            color=selected_value,
            height=600,
            title=f"チップデータ散布図（色: {selected_value}）",
        )


if __name__ == "__main__":
    app.run_server(debug=True)
