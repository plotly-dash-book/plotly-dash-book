import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")
# mapboxのアクセストークンを読み込む
px.set_mapbox_access_token("< your-token >")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("北九州避難所マップ", style={"textAlign": "center"}),
                # ➊ テーブルの作成
                dash_table.DataTable(
                    id="kitakyushu-datatable",
                    style_cell={
                        "textAlign": "center",
                        "maxWidth": "80px",
                        "whiteSpace": "normal",
                        "minWidth": "80px",
                    },
                    fixed_rows={"headers": True, "data": 0},
                    style_table={"maxHeight": 800, "maxWidth": "100%"},
                    filter_action="native",
                    row_selectable="multi",
                    sort_action="native",
                    sort_mode="multi",
                    page_size=700,
                    virtualization=True,
                    columns=[
                        {"name": col, "id": col, "deletable": True}
                        for col in df.columns
                    ],
                    data=df.to_dict("records"),
                ),
            ],
            style={"height": 400, "width": "80%", "margin": "2% auto 5%"},
        ),
        # ➋ mapのコールバック先のGraphクラス
        dcc.Graph(id="kitakyushu-map"),
    ]
)

# ➌ コールバックの作成


@app.callback(
    # 出力先はGraphクラス
    Output("kitakyushu-map", "figure"),
    # 入力元はデータテーブル
    Input("kitakyushu-datatable", "columns"),
    Input("kitakyushu-datatable", "derived_virtual_data"),
)
def update_map(columns, rows):
    # ➍ フィルタした後のデータでデータテーブルを作成する
    dff = pd.DataFrame(rows, columns=[c["name"] for c in columns])
    # ➎ そのデータを地図に示す
    return px.scatter_mapbox(
        dff,
        lat="緯度",
        lon="経度",
        zoom=10,
        hover_data=["名称", "名称かな表記", "住所表記"],
        labels={"fontSize": 20},
    )


app.run_server(debug=True)
