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
                "whiteSpace": "normal",
                "minWidth": "80px",
            },
            fixed_rows={"headers": True, "data": 0},
            style_table={"maxHeight": 800, "maxWidth": "100%"},
            # ➊ セルの編集を可能。
            editable=True,
            # ➊ 列のフィルタリングを可能に。
            filter_action="native",
            # ➊ 行の消去を可能に。
            row_deletable=True,
            # ➊ 複数行の選択を可能に。
            row_selectable="multi",
            # ➊ 列のソートを可能に。
            sort_action="native",
            # ➊ ソートを複数列を条件で可能に。
            sort_mode="multi",
            # ➋ 引数columnsにテーブル作成のデータを渡す
            columns=[
                {"name": col, "id": col, "deletable": True, "selectable": True}
                for col in df.columns
            ],
            data=df.to_dict("records"),
            # ➌ 1ページのデータを10行に
            page_size=10,
            # ➍ データファイルをエクスポート
            export_format="csv",
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
