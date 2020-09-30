import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.express as px

gapminder = plotly.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="gapminder-dropdown",
            # ➊ 辞書内包表記で選択肢を作成
            options=[{"label": c, "value": c} for c in gapminder["country"].unique()],
            # ➋ 複数国をリストに入れ初期値を設定
            value=["Japan", "China", "United States"],
            # ➌ 複数選択を設定
            multi=True,
            style={"textAlign": "center"},
        )
    ],
    style={"width": "50%", "margin": "3% auto"},
)


if __name__ == "__main__":
    app.run_server(debug=True)
