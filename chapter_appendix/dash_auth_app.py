import dash
import dash_auth
import dash_html_components as html

# ➊ 実際に用いる場合、ユーザ名とパスワードはソースコードに載せず、
#    別ファイルもしくはデータベースに保存する。
pass_pair = {"plotly": "dash", "test": "test1"}

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ➋ ユーザ名、パスワードを設定する。
auth = dash_auth.BasicAuth(app, pass_pair)

app.layout = html.H1("Plotly Dash Bookへようこそ！", style={"textAlign": "center"})

if __name__ == "__main__":
    app.run_server(debug=True)
