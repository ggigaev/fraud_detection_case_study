import numpy as np
import pandas as pd
import pickle

import src.scrubbington as scrub

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import normalize


def get_data(datafile):
    df_orig = pd.read_json('data/data.json')

    feature_list = ['channels', 'fb_published', 'has_analytics', 'has_logo',
    'num_order', 'num_payouts', 'sale_duration2', 'show_map', 'user_age',
    'user_type', 'body_length', 'org_name_bool']

    df, y, X = scrub.scrub_everything(df_orig, feature_list)

    X = normalize(X)

    return X, y


if __name__ == '__main__':
    X, y = get_data('data/data.json')

    model = RandomForestClassifier(n_jobs=2, random_state=0)
    #
    # model = RndmFrst()
    model.fit(X, y)

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
