import dash
import dash_html_components as html
import dash_table
import pandas as pd

df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            style_cell={
                "textAlign": "center",
                "maxWidth": "80px",
                "minWidth": "80px",
                "whiteSpace": "normal",
            },
            fixed_rows={"headers": True},  # ➊ 縦スクロール時にヘッダを固定
            # fixed_columns={"headers": True, "data": 3},  # ➋ 横スクロール時に最初の3列を固定
            style_table={"minWidth": "100%"},  # ➌ テーブル大きさ対策
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
        )
    ]
)

app.run_server(debug=True)
