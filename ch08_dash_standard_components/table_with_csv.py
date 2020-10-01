import dash
import dash_html_components as html
import dash_table
import pandas as pd

# ➊ 福岡県の避難所データを読み込む
df = pd.read_csv("data/kitakyushu_hinanjo.csv", encoding="shift-jis")

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            # ➋ dfの列名をリストにして引数columnsに渡す
            columns=[{"name": col, "id": col} for col in df.columns],
            # ➌ dfのデータを辞書型にして引数dataに渡す
            data=df.to_dict("records"),
        )
    ]
)

app.run_server(debug=True)
