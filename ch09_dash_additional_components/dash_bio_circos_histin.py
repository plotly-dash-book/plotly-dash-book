import json
from urllib.request import urlopen

import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

data = urlopen(
    "https://raw.githubusercontent.com/"
    "plotly/dash-bio-docs-files/master/circos_graph_data.json"
).read()

circos_graph_data = json.loads(data)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                # ➊ グラフの種類を選択するRadioItemsコンポーネント
                dcc.RadioItems(
                    id="radio-value",
                    options=[
                        {"label": "ヒストグラム外側表示", "value": "ヒストグラム外側表示"},
                        {"label": "ヒストグラム内側表示", "value": "ヒストグラム内側表示"},
                    ],
                    value="ヒストグラム外側表示",
                )
            ],
            style={"textAlign": "center"},
        ),
        # ➋ Circosコンポーネント
        dashbio.Circos(id="circos", layout=circos_graph_data["GRCh37"]),
    ],
    style={"width": "60%", "margin": "5% auto"},
)

# ➌ 選択されたグラフのtracksを返り値とするコールバック
@app.callback(Output("circos", "tracks"), Input("radio-value", "value"))
def update_graph(selected_value):
    if selected_value == "ヒストグラム外側表示":
        return [
            {
                # ➍ グラフの種類の設定。外側にヒストグラム表示
                "type": "HISTOGRAM",
                # ➎ 表示グラフ用データ
                "data": circos_graph_data["histogram"],
            }
        ]
    return [
        {
            # ➏ 内側にヒストグラム表示
            "type": "HISTOGRAM",
            "data": circos_graph_data["histogram"],
            # ➐ configの設定でヒストグラムは内側に描画
            "config": {"innerRadius": 40, "outerRadius": 300},
        }
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
