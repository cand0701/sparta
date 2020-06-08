from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost',27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')
##SAVE
@app.route('/order', methods=['POST'])
def save():
    name = request.form['name']
    count = request.form['count']
    address = request.form['address']
    numbers = request.form['numbers']

    return jsonify({'result':'success', 'msg':'등록되었습니다.'})

##GET
@app.route('/order',methods=['GET'])
def listup():
    return jsonify({'result':'success', 'msg':"조회되었습니당"})

if(__name__ == "__main__"):
    app.run('0.0.0.0', port=5000, debug=True)