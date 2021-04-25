from flask import Flask, render_template, request
import os
from joblib import dump, load
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
import pandas as pd
from text_preprocess import spacy_tokenizer, clean_text
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
        res["review"] = clean_text(res["review"])
        df = pd.Series([res["review"]])
        # load the model
        model = load('text_classifier.joblib')
        pred = model.predict(df)
        print(pred)
        if pred[0] == 1:
            data = {"Sentiment": "positive"}
        else:
            data = {"Sentiment": "Negative"}
        return render_template("result.html", data=data, result=result)
    if request.method == 'GET':
        return "<h3> nothing to show </h3>"

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
