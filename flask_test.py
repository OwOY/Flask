from flask import Flask, jsonify
import requests
import pandas as pd
import json
import numpy as np
import pymongo

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/',methods = ['GET'])
def home():

    return 'hello world'


@app.route('/<col_num>',methods = ['GET'])
def test(col_num):
    col_num = str(col_num)
    col_name_dict = {}
    client = pymongo.MongoClient('127.0.0.1')
    db = client['d1xz_net']
    coll_names = db.list_collection_names(session=None)
    i = 1
    for col_name in coll_names:
        col_name_dict[str(i)] = col_name
        i += 1
    print(col_name_dict)
    # data = [data for data in col.find({}, {'_id':0})]
    data = [data for data in db[col_name_dict[col_num]].find({}, {'_id':0})]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)