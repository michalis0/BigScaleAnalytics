from flask import Flask, render_template, request
import os
from joblib import dump, load
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
import pandas as pd
from preprocess import preprocess
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(result.to_dict())
        res = result.to_dict()
        res["tenure"] = int(res["tenure"])
        res["MonthlyCharges"] = float(res["MonthlyCharges"])
        df = pd.DataFrame([res])
        # apply the preprocessing (one hot encoding, etc to the input)
        sample = preprocess(df)
        # load the model
        model = load('LR.joblib')
        pred = model.predict(sample)
        print(pred)
        if pred[0] == 1:
            data = {"churn": "Yes"}
        else:
            data = {"churn": "No"}
        return render_template("result.html", data=data, result=result)
    else:
        return "hello"

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
