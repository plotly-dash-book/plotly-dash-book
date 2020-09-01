import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # ❶ Checklistクラスに変更
        dcc.Checklist(
            options=[
                {"label": "東京", "value": "東京"},
                {"label": "北海道", "value": "北海道"},
                {"label": "静岡", "value": "静岡"},
                {"label": "愛知", "value": "愛知"},
                {"label": "京都", "value": "京都"},
            ],  # ➋ valueはリストに入れて渡す
            value=["京都"],
            style={"textAlign": "center"},
        )
    ],
    style={"width": "80%", "margin": "3% auto"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
