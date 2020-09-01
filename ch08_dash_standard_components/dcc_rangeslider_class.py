import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.RangeSlider(
            min=0,
            max=40,
            step=1,
            value=[10, 30],  # ➊ 複数の値をリストで渡す
            marks={i: f"{i}" for i in range(41) if i % 5 == 0},
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
