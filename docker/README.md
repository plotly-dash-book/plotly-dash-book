# Docker

## 事前準備

サンプルコードのリポジトリをCloneし、カレントディレクトリをCloneしたリポジトリに移動します。

```bash
git clone https://github.com/plotly-dash-book/plotly-dash-book.git
cd plotly-dash-book.git
```

## 1-4章

### Jupyter Notebook

次のコマンドを実行します。

```bash
docker run -v $PWD:/work -p 8888:8888 plotlydashbook/plotly-dash-book jupyter notebook
```

出力中の `http://` で始まるURLにブラウザでアクセスします。

### JupyterLab

次のコマンドを実行します。

```bash
docker run -v $PWD:/work -p 8888:8888 plotlydashbook/plotly-dash-book jupyter lab
```

出力中の `http://` で始まるURLにブラウザでアクセスします。

## 5-11章

[ch05_dash_intro/dash_getting_started_scatter.py](https://github.com/plotly-dash-book/plotly-dash-book/blob/master/ch05_dash_intro/dash_getting_started_scatter.py) の例で説明します。実行したいファイルに適宜置き換えてください。

Pythonスクリプトを書き換え、 `run_server` メソッドの引数 `host` に `"0.0.0.0"` を渡します。

```python
-    app.run_server(debug=True)
+    app.run_server(debug=True, host="0.0.0.0")
```

スクリプトを実行します。リポジトリのPathは `/work` からはじまります。

```bash
docker run -p 8050:8050 -v $PWD:/work plotlydashbook/plotly-dash-book python /work/ch05_dash_intro/dash_getting_started_scatter.py
```

Webアプリケーションはブラウザから `http://0.0.0.0:8050/` にアクセスします。
