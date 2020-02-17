import dash
from dash_canvas import DashCanvas

app = dash.Dash(__name__)

app.layout = DashCanvas()

if __name__ == "__main__":
    app.run_server(debug=True)
