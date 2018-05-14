# Pipeline
import src.scrubbington as scrb
import src.modelington as mdl
import src.evaluationton as eval

import pandas as pd
import pickle
import sys

# Models
# from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize


if __name__ == '__main__':

    # if len(sys.argv) == 2:
    #     model = sys.argv[1]
    # else:
    #     print ("please specify model")


    # Load Data
    df = pd.read_json('data/data.json')

    feature_list = ['channels', 'fb_published', 'has_analytics', 'has_logo',
    'num_order', 'num_payouts', 'sale_duration2', 'show_map', 'user_age',
    'user_type', 'body_length']

    # Clean the dataframe, returning the df, the feature matrix,
    # and the label vector
    df_clean, y, X = scrb.scrub_everything(df, feature_list)

    # y = normalize(y)

    X = normalize(X)

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # Choose a model that corresponds to modelington
    model = mdl.logistic(y_train, X_train)


    evaluation = eval.ModelEvaluation(model, X_test, y_test)

    print (evaluation.precision)


    #
    #
    # print (model.coef_)





    # with open('model.pkl', 'wb') as f:
    #
    #     # Write the model to a file.
    #     pickle.dump(model, f)
