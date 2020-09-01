import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go

gapminder = plotly.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [  # ➊ RangeSliderクラス
        dcc.RangeSlider(
            id="rangeslider-g",
            min=gapminder.year.min(),
            max=gapminder.year.max(),
            step=5,
            value=[1952, 1977, 2007],  # ➋ 3つの値
            pushable=True,  # ➌ ハンドルが交錯しない
            updatemode="drag",  # ドラッグ時点で値を更新する
        ),
        html.Div([dcc.Graph(id="gapminder-g")]),
    ],
    style={"width": "80%", "margin": "5% auto"},
)


@app.callback(
    dash.dependencies.Output("gapminder-g", "figure"),
    [dash.dependencies.Input("rangeslider-g", "value")],
)
def update_graph(years):
    # レンジスライダで選択された年のデータフレームを取得する
    gapminder_years = gapminder[gapminder.year.isin(years)]
    # 選択された年のグラフを格納するためのリスト
    traces = []
    # 選択された年の散布図を作成しリストに格納する
    for year in gapminder_years["year"].unique():
        df_year = gapminder_years[gapminder_years["year"] == year]
        traces.append(
            go.Scatter(
                x=df_year["gdpPercap"],
                y=df_year["lifeExp"],
                text=df_year["country"],
                mode="markers",
                opacity=0.7,
                name=str(year),
            )
        )
    # tracesに格納した散布図をtraceに渡したfigureを返り値とする
    return {
        "data": traces,
        "layout": go.Layout(
            xaxis={"type": "log", "title": "GDP Per Capita", "range": [2, 5]},
            yaxis={"title": "Life Expectancy", "range": [20, 90]},
            hovermode="closest",
        ),
    }


if __name__ == "__main__":
    app.run_server(debug=True)
