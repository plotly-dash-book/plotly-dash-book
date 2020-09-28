import dash
import dash_html_components as html

# ➊ Dashインスタンスを生成する
app = dash.Dash(__name__)

# ➋ コンポーネントをlayout属性に渡す
app.layout = html.H1("Hello Dash")

if __name__ == "__main__":
    # ➌ アプリケーションを起動する
    app.run_server(debug=True)
