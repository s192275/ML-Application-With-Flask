import numpy as np
from flask import Flask, request,jsonify, render_template, url_for
import pickle
import pymysql
import os


#def sql_connector():
#    conn = pymysql.connect(user = 'root', password = 'root', db = 'patient_infos', host = 'localhost')
#    c = conn.cursor()
#    return conn, c

app = Flask(__name__)
model_heart  = pickle.load(open("heart.pkl", "rb"))
model_diabetes = pickle.load(open("diabetes.pkl", "rb"))
model_thyroid = pickle.load(open("thyroid.pkl", "rb"))

@app.route("/")
def home():
    return render_template("main_page.html")

@app.route("/throid")
def throid_info():
    return render_template("thyroid_main_page.html")

@app.route("/heart")
def heart_info():
    return render_template("heart_disase_main_page.html")

@app.route("/diabetes")
def diabetes_info():
    return render_template("diabetes_main_page.html")

@app.route("/pred_heart", methods = ["GET", "POST"])
def heart_predict():
    if request.method == 'POST':
        #conn, c = sql_connector()
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model_heart.predict(features)
        age = float_features[0]
        sex = float_features[1]
        cp = float_features[2]
        trestbps = float_features[3]
        chol = float_features[4]
        fbs = float_features[5]
        restecg = float_features[6]
        thalach = float_features[7]
        exang = float_features[8]
        oldpeak = float_features[9]
        slope = float_features[10]
        ca = float_features[11]
        thal = float_features[12]
        #c.execute("INSERT INTO patients (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal))
        #conn.commit()
        #conn.close()
        #c.close()
        if prediction == 1:
            a = "You probably have a heart disase!..."
            return render_template("heart_disase_predict.html", prediction_text = a)
        if prediction == 0:
            b = "You probably don't have a heart disase!..."
            return render_template("heart_disase_predict.html", prediction_text = b)
    return render_template("heart_disase_predict.html")

@app.route("/pred_diabetes", methods = ["GET", "POST"])
def diabetes_predict():
    if request.method == 'POST':
        #conn, c = sql_connector()
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model_diabetes.predict(features)
        highbp = float_features[0]
        highchol = float_features[1]
        cholcheck = float_features[2]
        bmi = float_features[3]
        smoker = float_features[4]
        stroke = float_features[5]
        heartdisaseorattack = float_features[6]
        physactivity = float_features[7]
        fruits = float_features[8]
        veggies = float_features[9]
        hvyalcoholconsump = float_features[10]
        anyhealthcare = float_features[11]
        nodocbccost = float_features[12]
        genhlth = float_features[13]
        menthlth = float_features[14]
        physhlth = float_features[15]
        diffwalk = float_features[16]
        sex = float_features[17]
        age = float_features[18]
        #c.execute("INSERT INTO patients (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal))
        #conn.commit()
        #conn.close()
        #c.close()
        if prediction == 1:
            a = "You have probably diabetes!..."
            return render_template("diabetes_disase_prediction.html", prediction_text = a)
        if prediction == 0:
            b = "You probably don't have diabetes!..."
            return render_template("diabetes_disase_prediction.html", prediction_text = b)
    return render_template("diabetes_disase_prediction.html")

@app.route("/pred_thyroid", methods=["GET", "POST"])
def thyroid_predict():
    if request.method == 'POST':
        #conn, c = sql_connector()
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model_thyroid.predict(features)
        age = float_features[0]
        sex = float_features[1]
        onthyroxine = float_features[2]
        queryonthyroxine = float_features[3]
        onantithyroidmedication = float_features[4]
        sick = float_features[5]
        pregnant = float_features[6]
        thyroidsurgery = float_features[7]
        i131treatment = float_features[8]
        queryhypothyroid = float_features[9]
        queryhyperthyroid = float_features[10]
        lithium = float_features[11]
        goitre = float_features[12]
        hypopituitary = float_features[13]
        psych = float_features[14]
        tsh = float_features[15]
        t3 = float_features[16]
        tt4 = float_features[17]
        t4u = float_features[18]
        referralsource = float_features[19]
        #c.execute("INSERT INTO patients (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal))
        #conn.commit()
        #conn.close()
        #c.close()
        if prediction == 1:
            a = "You have probably diabetes!..."
            return render_template("thyroid_disase_prediction.html", prediction_text = a)
        if prediction == 0:
            b = "You probably don't have diabetes!..."
            return render_template("thyroid_disase_prediction.html", prediction_text = b)
    return render_template("thyroid_disase_prediction.html")
    
if __name__ == "__main__":
    app.run(debug=True)