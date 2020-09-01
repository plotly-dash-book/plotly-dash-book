import dash
import dash_html_components as html
import dash_table
import pandas as pd

df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            page_size=700,  # ➊ 1ページの表示行数
            virtualization=True,  # ➋ 仮想化
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
        )
    ]
)

app.run_server(debug=True)
