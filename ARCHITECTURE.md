# 📊 Social Media Addiction Detector - Complete Workflow

## 🔄 Data Flow & Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     RAW DATASET (CSV)                           │
│          Students Social Media Addiction.csv                    │
│  • 1054 students                                                │
│  • 8 features + 1 target variable                              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │   EDA_Feature_engineering.ipynb      │
        │                                      │
        │  • Remove irrelevant columns (ID)   │
        │  • Handle missing values            │
        │  • Remove duplicates                │
        │  • Label encode categories          │
        │  • Create visualizations            │
        │  • Correlation analysis             │
        └──────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │   cleaned_student_social_media_      │
        │   addiction.csv                      │
        │  (Ready for ML training)             │
        └──────────────────────────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │    model_training.ipynb              │
        │                                      │
        │  • Train 7 different models         │
        │  • Hyperparameter tuning (SVR)      │
        │  • Model evaluation & comparison    │
        │  • Select best model (Random Forest)│
        │  • Save model & scaler              │
        └──────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
   best_model.pkl                      scaler.pkl
   (Random Forest)                      (StandardScaler)
        │                                     │
        └──────────────────┬──────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │          Flask Web App               │
        │          (app.py)                    │
        │                                      │
        │  Routes:                            │
        │  • GET  /  → Serve Web UI           │
        │  • POST /predict → Make predictions │
        └──────────────────────────────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
   User Input Form               Prediction Engine
   (index.html)               • Encode categories
   • Gender                   • Scale features
   • Academic Level           • Get prediction
   • Country                  • Classify level
   • Usage Hours              • Return results
   • Sleep Quality
   • Anxiety Level
   • Self-Esteem
   • Motivation Loss
        │                                     │
        └──────────────────┬──────────────────┘
                           │
                           ▼
        ┌──────────────────────────────────────┐
        │      Addiction Score & Level        │
        │    with Color-coded Results         │
        │  • Score (0-100)                    │
        │  • Level (Low/Moderate/High/Severe)│
        │  • Personalized Message             │
        └──────────────────────────────────────┘
```

## 📁 File Structure & Relationships

```
Student-Socail-media-addiction/
│
├─ Notebooks/
│  ├─ EDA_Feature_engineering.ipynb  ───────┐
│  │  Input: Students Social Media Addiction.csv
│  │  Output: cleaned_student_social_media_addiction.csv
│  │
│  ├─ model_training.ipynb  ────────────────┐
│  │  Input: cleaned_student_social_media_addiction.csv
│  │  Outputs: best_model.pkl, scaler.pkl
│  │
│  ├─ Students Social Media Addiction.csv  (Raw Data)
│  └─ cleaned_student_social_media_addiction.csv  (Processed)
│
├─ templates/
│  └─ index.html  ◄─── Web UI Template
│
├─ app.py  ◄─────────── Flask Server
│  ├─ Loads: best_model.pkl, scaler.pkl
│  ├─ Serves: index.html
│  └─ Handles: /predict endpoint
│
├─ best_model.pkl  ◄─── Random Forest Model (R² = 0.9829)
├─ scaler.pkl  ◄─────── StandardScaler for preprocessing
├─ requirements.txt  ◄─ Python Dependencies
└─ PROJECT_REVIEW.md  ◄─ Documentation
```

## 🎯 Input Features (8 Total)

### Categorical Features (3):
```
Gender
├── Male (encoded: 0)
├── Female (encoded: 1)
└── Other (encoded: 2)

Academic_Level
├── High School (encoded: 0)
├── Bachelor (encoded: 1)
├── Master (encoded: 2)
└── PhD (encoded: 3)

Country
├── USA (encoded: 0)
├── UK (encoded: 1)
├── Canada (encoded: 2)
├── Australia (encoded: 3)
├── India (encoded: 4)
├── Pakistan (encoded: 5)
├── Germany (encoded: 6)
├── France (encoded: 7)
└── Other (encoded: 8)
```

### Numeric Features (5):
```
Daily_Usage_Hours: 0-24 (hours)
Sleep_Quality: 1-10 (scale)
Social_Anxiety: 1-10 (scale)
Self_Esteem: 1-10 (scale)
Motivation_Loss: 1-10 (scale)
```

## 🧠 Model Information

### Best Model: Random Forest Regressor
- **R² Score**: 0.9829 (98.29% accuracy)
- **Type**: Ensemble Learning
- **Hyperparameters**: 
  - n_estimators: 100 trees
  - random_state: 42
  - max_depth: default

### Alternative Models Trained:
1. Linear Regression (R² = 0.9617)
2. Ridge Regression (R² = 0.9618)
3. Lasso Regression (R² = 0.9561)
4. ElasticNet Regression (R² = 0.9577)
5. SVR - Support Vector Regression (R² = 0.9735)
6. Tuned SVR (GridSearchCV) (R² = 0.9781)

## 🎨 Web UI Color Coding

```
Addiction Score Range        Level           Color   Message
─────────────────────────────────────────────────────────────
0-25                        Low            🟢 Green   Healthy usage
25-50                       Moderate       🟡 Yellow  Consider reducing time
50-75                       High           🟠 Orange  Seek help
75-100                      Severe         🔴 Red     Professional help needed
```

## 🔍 Data Preprocessing Steps

1. **Load Data** → Read CSV file
2. **Clean Data** → Remove Student_ID, handle nulls, remove duplicates
3. **Exploratory Analysis** → Value counts, distributions, correlations
4. **Feature Engineering** → Label encoding for categories
5. **Scaling** → StandardScaler normalization
6. **Model Training** → Train multiple algorithms
7. **Model Selection** → Choose best performer (Random Forest)
8. **Serialization** → Save model & scaler with joblib

## 🚀 Deployment Checklist

- ✅ Data cleaning complete
- ✅ Models trained & evaluated
- ✅ Best model selected & saved
- ✅ Feature scaler saved
- ✅ Flask app configured
- ✅ Web UI designed & responsive
- ✅ Input validation implemented
- ✅ Error handling added
- ✅ Documentation complete
- ✅ Ready for deployment

---
**Version**: 1.0  
**Status**: Production Ready ✅  
**Last Updated**: December 15, 2025
