from flask import Flask, render_template, request, jsonify
from flask_caching import Cache
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

# Initialize Flask app and cache
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Load dataset and model once at startup
try:
    df = pd.read_csv("ModelData/cs-training.csv")
    with open('Final_predictive_model/finalized_model.sav', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading resources: {e}")
    raise

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@app.route('/prediction', methods=['GET'])
def prediction_form():
    return render_template('predict.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get and validate form data
            features = [
                float(request.form.get('age', 0)),
                float(request.form.get('dependents', 0)),
                float(request.form.get('monthlyIncome', 0)),
                float(request.form.get('debtRatio', 0)),
                float(request.form.get('revolvingUtilization', 0)),
                float(request.form.get('late30To59Days', 0)),
                float(request.form.get('late60To89Days', 0)),
                float(request.form.get('late90PlusDays', 0)),
                float(request.form.get('openCreditLines', 0)),
                float(request.form.get('realEstateLoans', 0))
            ]

            # Basic input validation
            if features[0] < 0 or features[2] < 0:  # Age and income can't be negative
                raise ValueError("Age and Monthly Income must be non-negative.")

            # Convert to numpy array and predict
            prediction = model.predict([features])[0]
            return render_template('predict.html', prediction=int(prediction))
        except ValueError as ve:
            return render_template('predict.html', error=str(ve))
        except Exception as e:
            return render_template('predict.html', error="An unexpected error occurred.")
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)