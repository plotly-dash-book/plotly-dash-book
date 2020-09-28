import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("5つの四角形を並べたアプリケーション"),
        html.Div(
            [
                html.Div(className="roundsqlime columns"),
                html.Div(className="roundsqlime columns"),
            ]
        ),
        html.Div(
            [
                html.Div(className="roundsqblue columns"),
                html.Div(className="roundsqblue columns"),
                html.Div(className="roundsqblue columns"),
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
