import boto3
import botocore
import pickle


def load_dataset():
    return 'data/data.tsv'


def load_model(model_name):
    file = open(model_name, 'rb')
    print('loading model')
    model = pickle.load(file)
    print('model loaded')
    file.close()

    return model


def store_model(reg, model_name):
    file = open(model_name, 'wb')
    pickle.dump(reg, file)

    file.close()


class Store:
    store = {}

    def get(cls, model_name):
        if model_name in cls.store.keys():
            return cls.store[model_name]
        else:
            model = load_model(model_name)
            cls.store[model_name] = model

            return model

