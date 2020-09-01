import dash
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go

gapminder = plotly.data.gapminder()
gapminder = gapminder[gapminder["year"] == 2007]

# ➊ figureの作成
fig = go.Figure()
for c in gapminder.continent.unique():
    fig.add_trace(
        go.Scatter(
            x=gapminder[gapminder["continent"] == c]["gdpPercap"],
            y=gapminder[gapminder["continent"] == c]["pop"],
            name=c,
            mode="markers",
            marker={"size": gapminder[gapminder["continent"] == c]["lifeExp"] / 2},
            text=gapminder[gapminder["continent"] == c]["country"],
        )
    )
fig.update_layout(
    xaxis={"type": "log", "title": "gdpPercap"},
    yaxis={"type": "log", "title": "pop"},
    title="Gapminder",
)


app = dash.Dash(__name__)

app.layout = dcc.Graph(
    # ➋ figureにfigを渡す
    figure=fig
)

if __name__ == "__main__":
    app.run_server(debug=True)
