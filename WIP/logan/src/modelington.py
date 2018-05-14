from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def logistic(y_train, X_train):

    lr = LogisticRegression()

    lr.fit(X_train,y_train)

    return lr
