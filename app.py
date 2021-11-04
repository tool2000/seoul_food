from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form)
        text = request.form['shop']
        con = sqlite3.connect("./seoul_food.db")
        cc = con.cursor()
        cc.execute(f"SELECT * FROM shop WHERE shopName LIKE '%{text}%'")
        result = cc.fetchall()
        return render_template('index.html', data=result)


@app.route('/notice')
def notice():

    result = "피자 8조각을 4명이서 나눠 먹으면? 답은: "
    piece = 8/4
    result = result + str(piece)

    return result

@app.route('/birth')
def birth():
    return '당신의 생일을 축하합니다~!!'

@app.route('/main')
def main():
    return "안녕하세요."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888)
    #app.run(debug=True, port=5000)

