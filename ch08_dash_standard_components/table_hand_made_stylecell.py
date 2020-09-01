import dash
import dash_table

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    fill_width=False,
    columns=[
        {"name": "number", "id": "number"},
        {"name": "region", "id": "area"},
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
    # ➊ テーブル全体のセルのスタイルを定義（横幅、文字の大きさ、文字の揃え位置）
    style_cell={"width": 160, "fontSize": 24, "textAlign": "center"},
)

app.run_server(debug=True)
