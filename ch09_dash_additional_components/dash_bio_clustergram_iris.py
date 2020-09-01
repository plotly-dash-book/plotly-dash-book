import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html
import plotly

iris = plotly.data.iris()
iris = iris.drop("species", 1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            figure=dashbio.Clustergram(
                data=iris.values,  # ➊ グラフ作成に用いる値の設定
                column_labels=list(iris.columns.values),  # ➋ 列ラベルの設定
                width=800,  # ➋ 横幅の設定
                height=800,  # ➋ 高さの設定
                # ➋ ヒートマップの配色
                color_map=[[0.0, "white"], [0.5, "gray"], [1.0, "black"]],
                # ➋ デントログラムの高さの設定（行側、列側、ヒートマップ比）
                display_ratio=[0.3, 0.1],
            )
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
