import dash
import dash_html_components as html
import dash_table
import pandas as pd

df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            # ➊ 引数 style_cell
            style_cell={
                "textAlign": "center",  # テキストを中央寄せ
                "maxWidth": "80px",  # ➋ 最大横幅
                "minWidth": "80px",  # ➌ 最小横幅
                "whiteSpace": "normal",  # ➍ 文字を折り返し表示
            },
            columns=[{"name": col, "id": col} for col in df.columns],
            data=df.to_dict("records"),
        )
    ]
)

app.run_server(debug=True)
