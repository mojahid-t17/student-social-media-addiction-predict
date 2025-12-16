# Social Media Addiction Detector - Project Review

## Project Structure
```
Student-Socail-media-addiction/
├── Notebooks/
│   ├── EDA_Feature_engineering.ipynb          # Data cleaning & preprocessing
│   ├── model_training.ipynb                    # Model training & evaluation
│   ├── Students Social Media Addiction.csv    # Raw dataset
│   └── cleaned_student_social_media_addiction.csv  # Cleaned data
├── templates/
│   └── index.html                             # Flask web UI
├── app.py                                     # Flask application
├── best_model.pkl                             # Trained Random Forest model
├── scaler.pkl                                 # StandardScaler for preprocessing
├── requirements.txt                           # Python dependencies
├── flask_requirements.txt                     # Flask-specific dependencies
├── FLASK_README.md                            # Flask app documentation
└── PROJECT_REVIEW.md                          # This file
```

## Dataset Features (8 inputs + 1 target)

### Input Features (used in Flask UI):
1. **Gender** (Categorical: Male, Female, Other)
2. **Academic_Level** (Categorical: High School, Bachelor, Master, PhD)
3. **Country** (Categorical: USA, UK, Canada, Australia, India, Pakistan, Germany, France, Other)
4. **Daily_Usage_Hours** (Numeric: 0-24 hours)
5. **Sleep_Quality** (Numeric: 1-10)
6. **Social_Anxiety** (Numeric: 1-10)
7. **Self_Esteem** (Numeric: 1-10)
8. **Motivation_Loss** (Numeric: 1-10)

### Target Feature:
- **Addicted_Score** (Numeric: 0-100) - Predicted by the model

## Data Processing Pipeline

### EDA_Feature_engineering.ipynb
- ✅ Load raw CSV data
- ✅ Remove Student_ID column (irrelevant)
- ✅ Check and handle missing values
- ✅ Remove duplicate rows
- ✅ Separate categorical and numeric columns
- ✅ Analyze value counts for categorical features
- ✅ Create visualizations (bar plots, histograms, heatmaps)
- ✅ Label encode categorical columns
- ✅ Generate correlation matrix
- ✅ Save cleaned data as `cleaned_student_social_media_addiction.csv`

### model_training.ipynb
- ✅ Load cleaned data
- ✅ Split into train/test sets (80/20)
- ✅ Scale features using StandardScaler
- ✅ Train 7 different models:
  - Linear Regression (R² = 0.9617)
  - Ridge Regression (R² = 0.9618)
  - Lasso Regression (R² = 0.9561)
  - ElasticNet (R² = 0.9577)
  - SVR (R² = 0.9735)
  - Tuned SVR (R² = 0.9781)
  - **Random Forest (R² = 0.9829)** ⭐ BEST MODEL
- ✅ Save best model as `best_model.pkl`
- ✅ Save scaler as `scaler.pkl`
- ✅ Make predictions and visualize results

## Flask Web Application

### app.py Features:
- ✅ Loads best-trained model (Random Forest with R² = 0.9829)
- ✅ Handles categorical variable encoding (Gender, Academic_Level, Country)
- ✅ Scales numeric inputs using saved StandardScaler
- ✅ Makes predictions on user input
- ✅ Classifies addiction levels with color coding
- ✅ Error handling for missing model files
- ✅ Dynamic file path detection for model/scaler

### index.html (Web UI) Features:
- ✅ Modern gradient design (Purple theme)
- ✅ Responsive layout (mobile & desktop)
- ✅ Input validation
- ✅ Real-time value display for sliders
- ✅ Loading animation during prediction
- ✅ Color-coded results:
  - 🟢 Green: Low addiction (0-25)
  - 🟡 Yellow: Moderate addiction (25-50)
  - 🟠 Orange: High addiction (50-75)
  - 🔴 Red: Severe addiction (75-100)
- ✅ Personalized messages & recommendations

## Running the Application

### Prerequisites:
```bash
pip install -r requirements.txt
```

### Start Flask Server:
```bash
python app.py
```

### Access Web UI:
- Open browser: `http://localhost:5000`

## Model Performance Comparison

| Model | R² Score | MSE |
|-------|----------|-----|
| Random Forest ⭐ | 0.9829 | Lowest |
| Tuned SVR | 0.9781 | - |
| SVR | 0.9735 | - |
| Ridge Regression | 0.9618 | - |
| Linear Regression | 0.9617 | - |
| ElasticNet | 0.9577 | - |
| Lasso Regression | 0.9561 | - |

## Files Status

✅ **Complete & Ready**:
- Data cleaning notebook (EDA_Feature_engineering.ipynb)
- Model training notebook (model_training.ipynb)
- Flask application (app.py)
- Web UI template (index.html)
- Trained model (best_model.pkl)
- Feature scaler (scaler.pkl)
- Requirements file (requirements.txt)

## Recent Updates

1. ✅ Updated app.py to search multiple paths for model/scaler files
2. ✅ Added EDA column validation cell in notebook
3. ✅ HTML UI matches all 8 input features exactly
4. ✅ Model encoding/scaling matches training pipeline

## Next Steps (Optional Enhancements)

- [ ] Deploy to cloud (Heroku, AWS, Azure)
- [ ] Add user data persistence
- [ ] Create analytics dashboard
- [ ] Generate detailed PDF reports
- [ ] Add mobile app wrapper
- [ ] Implement user authentication
- [ ] Create API for external integrations

---
**Last Updated:** December 15, 2025
**Project Status:** ✅ READY FOR PRODUCTION
