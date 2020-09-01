import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Link("/test", href="/test"),  # ➊
        html.Br(),
        dcc.Link("/test2", href="/test2"),
        html.Br(),
        dcc.Link("/test3", href="/test3"),
        html.Br(),
        dcc.Link("home", href="/"),
    ],
    style={"fontSize": 30, "textAlign": "center"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
