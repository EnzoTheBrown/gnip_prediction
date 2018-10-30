from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from gnip.models.store import store_model


def train(X, y):
    return LinearRegression().fit(X, y)


def predict(reg, X):
    return reg.predict(X)


def compile(df, input_features, output_features, model_name):
    X = df[input_features]
    y = df[output_features]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    reg = train(X_train, y_train)

    store_model(reg, model_name)

    print 'value:'
    print y_test
    print 'prediction'
    y_hat = predict(reg, X_test)
    print y_hat
    print 'score'
    return r2_score(y_test, y_hat)

