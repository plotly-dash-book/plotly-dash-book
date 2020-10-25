import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # スライダの作成
        dcc.Slider(
            id="myslider",
            min=-10,  # 最小値
            max=100,  # 最大値
            step=1,  # 目盛
            value=50,  # 初期値
            # ➊ スライダの目盛の作成。数値に対して割り当てる。
            marks={
                -10: {"label": "-10度", "style": {"color": "blue", "fontSize": 30},},
                0: {"label": "0", "style": {"fontSize": 40}},
                25: "25度",
                50: {"label": "50度", "style": {"fontSize": 50}},
                75: "75度",
                100: {"label": "100度", "style": {"fontSize": 40, "color": "red"},},
            },
            dots=True,
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
