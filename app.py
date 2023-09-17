# Flaskのインポート
from flask import Flask, request,render_template
import time

app = Flask(__name__)

# ---------------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# GETリクエスト用のエンドポイント
@app.route('/get_method', methods=['GET'])
def get_method():
    # 処理時間を計測（シミュレーションのために2秒待機）
    # time.sleep(2)
    return "This is a GET request."

# POSTリクエスト用のエンドポイント
@app.route('/post_method', methods=['POST'])
def post_method():
    # 処理時間を計測（シミュレーションのために2秒待機）
    # time.sleep(2)
    return "This is a POST request."

if __name__ == '__main__':
    app.run(debug=True)
