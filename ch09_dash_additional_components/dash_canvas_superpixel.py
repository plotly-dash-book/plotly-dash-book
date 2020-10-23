import dash
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash_canvas import DashCanvas
from dash_canvas.utils import (
    array_to_data_url,
    image_string_to_PILImage,
    parse_jsonstring,
    superpixel_color_segmentation,
)
from skimage import color, io

image_path = "img/bird2.png"
default_image = io.imread(image_path)
image_string = array_to_data_url(default_image)
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                DashCanvas(
                    id="first-image",
                    filename=image_string,
                    width=500,
                    lineWidth=5,
                    lineColor="lime",
                    goButtonTitle="remove",
                )
            ],
            style={"float": "left", "width": "40%"},
        ),
        html.Div(
            [html.Img(id="remove-background")], style={"float": "left", "width": "40%"},
        ),
    ]
)


@app.callback(
    Output("remove-background", "src"),
    Input("first-image", "json_data"),
    Input("first-image", "image_content"),
)
def remove_background(json_data, image):
    if json_data:
        # ➊ imageが値をもつ場合、それを基に画像のnumpy.ndarrayに変換する
        if image:
            image_array = image_string_to_PILImage(image)
            image_array = np.asarray(image_array)
        # imageが値をもたない場合、imreadで画像を読み込む
        else:
            image_array = io.imread(image_path)
        # ➋ 画像のアレイのサイズを変数shapeに代入する
        shape = image_array.shape[:2]

        # ➌ 書き込みのJSONデータをパースし、ブール値に変換する
        try:
            mask = parse_jsonstring(json_data, shape=shape)
        except IndexError:
            raise PreventUpdate

        if mask.sum() > 0:  # ➍
            seg = superpixel_color_segmentation(image_array, mask)
        else:
            seg = np.ones(shape)
        filled_image = np.copy(image_array)
        filled_image[np.logical_not(seg)] = np.array(
            [255, 255, 255], dtype="uint8"
        )  # ➎
        return array_to_data_url(filled_image)  # ➏

    else:
        PreventUpdate


if __name__ == "__main__":
    app.run_server(debug=True)
