import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from joblib import dump, load

def preprocess(df):
    X = df[["tenure", "MonthlyCharges"]]
    one_hot = load('one_hot.joblib')
    one_hot_features = one_hot.transform(df[["gender", "PhoneService", "TechSupport", "StreamingTV", "PaperlessBilling"]])
    one_hot_features = pd.DataFrame(one_hot_features.toarray())
    X = pd.concat((X, one_hot_features), axis=1)
    return X
