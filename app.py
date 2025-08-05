from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from end_to_end_project.pipeline.prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('result.html', 
                                 prediction = float(predict[0]),
                                 fixed_acidity = fixed_acidity,
                                 volatile_acidity = volatile_acidity,
                                 citric_acid = citric_acid,
                                 residual_sugar = residual_sugar,
                                 chlorides = chlorides,
                                 free_sulfur_dioxide = free_sulfur_dioxide,
                                 total_sulfur_dioxide = total_sulfur_dioxide,
                                 density = density,
                                 pH = pH,
                                 sulphates = sulphates,
                                 alcohol = alcohol)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=True)