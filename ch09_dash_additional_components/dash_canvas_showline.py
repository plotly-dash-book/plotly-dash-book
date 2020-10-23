import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
from dash_canvas import DashCanvas
from dash_canvas.utils import array_to_data_url, parse_jsonstring_rectangle
from skimage import io

filename = array_to_data_url(io.imread("img/bird1.png"))
pen_color = ["black", "lime", "red", "blue", "yellow"]
columns = ["width", "height", "left", "top"]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                # 線色を変更するラジオアイテム
                dcc.RadioItems(
                    id="color-radio",
                    options=[{"value": c, "label": c} for c in pen_color],
                    value="lime",
                ),
                # キャンバス
                DashCanvas(
                    id="first-image",
                    image_content=filename,
                    width=800,
                    lineWidth=5,
                    goButtonTitle="to_table",
                ),
            ],
            style={"float": "left", "width": "70%"},
        ),
        html.Div(
            [  # 長方形のデータのみを表示するテーブル
                dash_table.DataTable(
                    id="showTable",
                    columns=[{"name": i, "id": i} for i in columns],
                    style_cell={
                        "textAlign": "center",
                        "whiteSpace": "normal",
                        "maxWidth": "80px",
                        "minWidth": "80px",
                    },
                    export_format="csv",
                )
            ],
            style={"display": "inline-block", "marginRight": "5%", "width": "25%",},
        ),
    ]
)

# ➊ 線色を更新するコールバック
@app.callback(Output("first-image", "lineColor"), Input("color-radio", "value"))
def update_color(selected_color):
    return selected_color


# ➋ 長方形のデータのみをテーブルに表示するコールバック
@app.callback(Output("showTable", "data"), Input("first-image", "json_data"))
def showLine(json_data):

    if not json_data:
        raise dash.exceptions.PreventUpdate
    data = parse_jsonstring_rectangle(json_data)
    if len(data):
        df = pd.DataFrame(data, columns=columns)
        return df.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
