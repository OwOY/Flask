from flask import Flask, jsonify
import requests
import pandas as pd
import json
import numpy as np

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

test =[{'happy':'1',
     'unhappy':'2'},
        {'QQ':'3',
     'XD':'4',
    'ohya':'小夫',
     'ohno':'大雄'}]

tour = []
df = pd.read_csv('tour.csv')
df = df.to_json()
df = json.loads(df)
for i in range(len(df['Type'])):
    data = {}
    for d in df:
        data[d]=df[d][str(i)]
    tour.append(data)
thistour = tour

@app.route('/',methods = ['GET'])

def home():
    return 'hello world'

@app.route('/test',methods = ['GET'])

def index():
    return jsonify(test)

@app.route('/tour',methods = ['GET'])

def tour():
    return jsonify(thistour)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)