from flask import Flask,render_template,request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow 
from tensorflow.keras.models import load_model
import sqlite3

app = Flask(__name__)
skl = pickle.load(open('scaler.pkl','rb'))
model = load_model('Model.h5')
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    chestPain = int(request.form['chestPain'])
    bloodPressure = int(request.form['bloodPressure'])
    cholestrol = int(request.form['cholestrol'])
    bsugar = int(request.form['bsugar'])
    ecg = int(request.form['ecg'])
    heartRate = int(request.form['heartRate'])
    cPain = int(request.form['cPain'])
    STdepression = int(request.form['STdepression'])
    slopeST = int(request.form['slopeST'])
    majorVessel = int(request.form['majorVessel'])
    ThalScore = int(request.form['ThalScore'])

    x = np.array([age,gender,chestPain,bloodPressure,cholestrol,bsugar,ecg,heartRate,cPain,STdepression,slopeST,majorVessel,ThalScore]).reshape(1,-1)
    x = skl.transform(x)
    y = model.predict(x)
    res = y[0]
    resultDB = res[0]
    with sqlite3.connect('dataset.db') as con:
        cur = con.cursor()
        cur.execute("INSERT into Heartdisease(age,gender,chestPain,bloodPressure,cholestrol,bsugar,ecg,heartRate,cPain,STdepression,slopeST,majorVessel,ThalScore, result) values (?,?,?,?,?,?,?,?,?,?,?,?,?)", (age,gender,chestPain,bloodPressure,cholestrol,bsugar,ecg,heartRate,cPain,STdepression,slopeST,majorVessel,ThalScore, resultDB))
        con.commit()
    con.close()

    if(res[0]<0.5):
        return render_template('index.html', prediction="You are safe!!..Chances are: {}".format(res[0]*100))
    else:
        return render_template('index.html', prediction="Consult nearest doctor ASAP!!..Chances are: {}".format(res[0]*100))


if __name__ == '__main__':
    app.debug=True
    app.run()