import dash
import dash_table

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    fill_width=False,
    columns=[
        {"name": "number", "id": "number"},
        {"name": "area", "id": "area"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri"},
    ],
    data=[
        {"number": 0, "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    # ➊ 列全体のスタイル
    style_cell_conditional=[
        {  # ➍ 条件は辞書で渡す
            "if": {"column_id": "number"},
            # ➎ 条件を満たした場合の装飾
            "fontSize": 24,
            "backgroundColor": "#FFEEE4",
        }
    ],
    # ➋ ヘッダーのスタイル
    style_header_conditional=[
        {"if": {"column_id": "area"}, "textAlign": "center", "width": 150},
        {"if": {"column_id": "tsuyu-iri"}, "backgroundColor": "#FBFFB9"},
    ],
    # ➌ データ部分のスタイル
    style_data_conditional=[
        {"if": {"row_index": "odd"}, "backgroundColor": "#FBFFB9"},
        # ➏ fileter_queryを利用する場合、条件を""で囲って渡す
        {
            "if": {"column_id": "tsuyu-iri", "filter_query": "{number} > 3"},
            "backgroundColor": "#41D3BD",
        },
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
