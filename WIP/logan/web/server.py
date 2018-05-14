import sys
import pickle
from flask import Flask, render_template, request, jsonify, Response
import pandas as pd
import pymongo
from pymongo import MongoClient

import predict as prdct

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/score', methods=['POST'])
def score():
    # Just pulling from file for now
    samp = prdct.load_sample()
    clean, df, name = prdct.mini_clean(samp)
    probability = prdct.predict_probability(model, clean)
    prdct.db_insert(df, probability, table)

    return jsonify({'name':name, 'probability': probability})


if __name__ == '__main__':

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    client = MongoClient('localhost', 27017)

    db = client.prediction_db
    table = db.predictions

    app.run(host='0.0.0.0', port=3333, debug=True)
