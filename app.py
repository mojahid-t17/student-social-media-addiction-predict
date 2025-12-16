from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

app = Flask(__name__)

# Load the best model with better error handling
model_paths = ['best_model.pkl', 'Notebooks/best_model.pkl', '../best_model.pkl']
model = None
for path in model_paths:
    try:
        model = joblib.load(path)
        print(f"Model loaded from: {path}")
        break
    except FileNotFoundError:
        continue

if model is None:
    print("ERROR: 'best_model.pkl' not found!")
    print("Searched in:", model_paths)
    print("Please run your Jupyter notebook to train and save the model first.")

# Load the scaler
scaler_paths = ['scaler.pkl', 'Notebooks/scaler.pkl', '../scaler.pkl']
scaler = None
for path in scaler_paths:
    try:
        scaler = joblib.load(path)
        print(f"Scaler loaded from: {path}")
        break
    except FileNotFoundError:
        continue

if scaler is None:
    print("WARNING: 'scaler.pkl' not found. Using default StandardScaler.")
    scaler = StandardScaler()

# Feature names (must match training data)
feature_names = ['Gender', 'Academic_Level', 'Country', 'Daily_Usage_Hours', 
                 'Sleep_Quality', 'Social_Anxiety', 'Self_Esteem', 'Motivation_Loss']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please train and save the model first.'
            }), 400
        
        data = request.json
        
        # Extract input values - all 11 features
        age = float(data.get('age', 0))
        gender = data.get('gender', '')
        academic_level = data.get('academic_level', '')
        country = data.get('country', '')
        daily_usage = float(data.get('daily_usage', 0))
        platform = data.get('platform', '')
        academic_perf = float(data.get('academic_perf', 0))
        sleep_hours = float(data.get('sleep_hours', 0))
        mental_health = float(data.get('mental_health', 0))
        relationship = data.get('relationship', '')
        conflicts = float(data.get('conflicts', 0))
        
        # Encode categorical variables
        gender_mapping = {'Male': 0, 'Female': 1, 'Other': 2}
        academic_mapping = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
        country_mapping = {
            'USA': 0, 'UK': 1, 'Canada': 2, 'Australia': 3, 
            'India': 4, 'Pakistan': 5, 'Germany': 6, 'France': 7, 'Other': 8
        }
        platform_mapping = {'Instagram': 0, 'TikTok': 1, 'Twitter': 2, 'Facebook': 3, 'YouTube': 4, 'Snapchat': 5, 'Other': 6}
        relationship_mapping = {'Single': 0, 'In Relationship': 1, 'Married': 2, 'Prefer Not to Say': 3}
        
        gender_encoded = gender_mapping.get(gender, 0)
        academic_encoded = academic_mapping.get(academic_level, 0)
        country_encoded = country_mapping.get(country, 0)
        platform_encoded = platform_mapping.get(platform, 0)
        relationship_encoded = relationship_mapping.get(relationship, 0)
        
        # Create feature array with all 11 features in correct order
        features = np.array([[
            age,                      # Age
            gender_encoded,           # Gender
            academic_encoded,         # Academic_Level
            country_encoded,          # Country
            daily_usage,              # Avg_Daily_Usage_Hours
            platform_encoded,         # Most_Used_Platform
            academic_perf,            # Affects_Academic_Performance
            sleep_hours,              # Sleep_Hours_Per_Night
            mental_health,            # Mental_Health_Score
            relationship_encoded,     # Relationship_Status
            conflicts                 # Conflicts_Over_Social_Media
        ]])
        
        # Scale features using the loaded scaler
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Determine addiction level
        if prediction < 5:
            level = "Good"
            color = "green"
            message = "Healthy usage pattern. Keep it up!"
        elif prediction < 8:
            level = "Addicted"
            color = "yellow"
            message = "You are moderately addicted. Consider reducing screen time."
        else:
            level = "Dangerous"
            color = "red"
            message = "Dangerous addiction level detected. Professional help is strongly recommended."
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2),
            'level': level,
            'color': color,
            'message': message
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
