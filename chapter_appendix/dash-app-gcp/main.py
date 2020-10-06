import dash
import dash_html_components as html

dash_app = dash.Dash(__name__)
app = dash_app.server

dash_app.layout = html.Div([html.H1("Hello Dash")])

if __name__ == "__main__":
    dash_app.run_server(debug=True)
