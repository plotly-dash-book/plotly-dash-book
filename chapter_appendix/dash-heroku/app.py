import os

import dash
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([html.H1("Hello World!")])

if __name__ == "__main__":
    app.run_server(debug=True)
