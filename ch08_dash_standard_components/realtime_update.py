import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

start = pd.Timestamp(datetime.datetime.now()).round("s") - datetime.timedelta(
    seconds=300
)

df = pd.DataFrame(
    {"price": np.random.randn(1000).cumsum()},
    index=pd.date_range(start, freq="s", periods=1000),
)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # ➊ タイトルは現在の時刻とn_clickの属性値を用いて作成する
        html.H1(id="realtime-title", style={"textAlign": "center"}),
        dcc.Graph(id="realtime-graph"),
        # ➋ Intervalクラスの引数intervalで更新間隔を設定・更新最大回数は100回
        dcc.Interval(id="realtime-interval", interval=1000, max_intervals=100),
    ]
)

# ➌ コールバックの作成
@app.callback(
    Output("realtime-title", "children"),
    Output("realtime-graph", "figure"),
    Input("realtime-interval", "n_intervals"),
)
def update_graph(n_intervals):

    # ➍ 現時点から120秒前までのデータを取得し、グラフを返す
    now = pd.Timestamp(datetime.datetime.now()).round("s")
    past = now - datetime.timedelta(seconds=120)

    plot_df = df.loc[past:now]

    # ➎ タイトルとグラフを戻り値とする
    return (
        f"live-update-chart: {now} / n_intervals: {n_intervals}",
        {"data": [go.Scatter(x=plot_df.index, y=plot_df["price"])]},
    )


if __name__ == "__main__":
    app.run_server(debug=True)
