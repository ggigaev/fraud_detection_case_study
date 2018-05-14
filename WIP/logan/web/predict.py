import pandas as pd
import pickle
import pymongo
from pymongo import MongoClient
import json

import src.scrubbington as scrub

from sklearn.preprocessing import normalize


def load_sample():
    df = pd.read_json("data/test_script_examples.json")
    return df.sample(1)

def mini_clean(df):

    df2 = scrub.scrub_datetime(df)

    df2['org_name_bool'] = len(df2['org_name']) == 0

    feature_list = ['channels', 'fb_published', 'has_analytics', 'has_logo',
    'num_order', 'num_payouts', 'sale_duration2', 'show_map', 'user_age',
    'user_type', 'body_length', 'org_name_bool']

    X = df2[feature_list].values

    return normalize(X), df2[feature_list], df2['name'].values[0]

def predict_probability(model, X):

    # Return the value for 'True' prediction
    return model.predict_proba(X)[0][1]

def db_insert(df, probability, db_table):

    df2 = df.assign(probability=probability)

    record = json.loads(df2.T.to_json())

    db_table.insert_one(record)



if __name__ == '__main__':

    client = MongoClient('localhost', 27017)

    db = client.prediction_db
    table = db.predictions

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    df_mini = load_sample()
    clean, df, name = mini_clean(df_mini)

    probability = predict_probability(model, clean)

    db_insert(df, probability, table)

    print (name, "\n", "Prediction: ", probability)
