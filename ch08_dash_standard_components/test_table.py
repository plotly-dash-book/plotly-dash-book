import dash
import dash_table

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    # ➊ 引数columnsにデータを渡す
    columns=[
        {"name": "number", "id": "number", "type": "text"},
        {"name": "region", "id": "area"},
        {"name": "tsuyu-iri", "id": "tsuyu-iri"},
    ],
    # ➋ 引数dataにデータを渡す
    data=[
        {"number": "# test", "area": "okinawa", "tsuyu-iri": "5/16"},
        {"number": 1, "area": "kyusyu-south", "tsuyu-iri": "5/31"},
        {"number": 2, "area": "kyusyu-north", "tsuyu-iri": "6/26"},
        {"number": 3, "area": "shikoku", "tsuyu-iri": "6/26"},
        {"number": 4, "area": "chugoku", "tsuyu-iri": "6/26"},
        {"number": 5, "area": "kinki", "tsuyu-iri": "6/26"},
    ],
    # ➌ テーブルを画面いっぱいに広げない
    fill_width=False,
    merge_duplicate_headers=True,
    style_data={"width": 160, "fontSize": 24, "textAlign": "center"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
