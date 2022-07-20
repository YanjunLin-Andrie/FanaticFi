import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # import pickle file of my model
    model = pickle.load(open('model.pkl', 'rb'))

    # import pickle file of my scaler
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    # For rendering results on HTML GUI
    init_features = [float(x) for x in request.form.values()]
    final_features = np.array([init_features])
    features_scaled = scaler.transform(final_features)
    prediction = model.predict(features_scaled)
    if prediction[0] == 1:
        result="The player you choose will be in the Top 15 picks"
    else:   
        result="The player you choose will rank 16 and below"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)




