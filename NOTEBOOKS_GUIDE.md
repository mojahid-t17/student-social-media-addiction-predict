# 📓 Jupyter Notebooks Documentation

## 1. EDA_Feature_engineering.ipynb
### Purpose: Data Exploration, Cleaning & Preprocessing

#### Workflow:
```
Cell 1-3:   Import libraries & load raw data
Cell 4:     Display dataset info & structure
Cell 5-8:   Remove irrelevant columns (Student_ID)
Cell 9-13:  Check & handle missing values
Cell 14-16: Identify & remove duplicate rows
Cell 17-20: Separate categorical vs numeric columns
Cell 21-25: Analyze value counts for each categorical feature
Cell 26-27: Visualize addiction score by gender (bar plot)
Cell 28-29: Distribution analysis of addiction scores
Cell 30-31: Label encode categorical columns
Cell 32:    Display statistical summary
Cell 33:    Correlation heatmap visualization
Cell 34:    Save cleaned data to CSV
Cell 35:    Print column info for Flask configuration
```

#### Key Outputs:
- `cleaned_student_social_media_addiction.csv` (cleaned dataset)
- Console output with column names & types for Flask configuration

#### Input Data Shape:
- Rows: ~1054 students
- Columns: 9 (8 features + 1 target)

#### Categorical Columns Identified:
- Gender (3 unique values)
- Academic_Level (4 unique values)
- Country (9 unique values)

#### Numeric Columns Identified:
- Daily_Usage_Hours
- Sleep_Quality
- Social_Anxiety
- Self_Esteem
- Motivation_Loss
- Addicted_Score (TARGET)

---

## 2. model_training.ipynb
### Purpose: Model Training, Evaluation & Selection

#### Workflow:
```
Cell 1:     Load cleaned CSV data
Cell 2:     Define features (X) and target (y)
Cell 3:     Display feature preview
Cell 4-5:   Train-test split (80/20) with StandardScaler
Cell 6-7:   Display data shapes
Cell 8:     Correlation matrix heatmap
Cell 9:     Feature scaling with StandardScaler
Cell 10:    Display scaled data
Cell 11-12: Train Linear Regression model
Cell 13-14: Evaluate Linear Regression (MSE, R²)
Cell 15-16: Train Ridge Regression model
Cell 17:    Display Ridge parameters
Cell 18-19: Evaluate Ridge Regression
Cell 20-21: Train Lasso Regression model
Cell 22:    Display Lasso parameters
Cell 23-24: Evaluate Lasso Regression
Cell 25-26: Train ElasticNet Regression model
Cell 27-28: Evaluate ElasticNet Regression
Cell 29-30: Train SVR (Support Vector Regression)
Cell 31-32: Evaluate SVR model
Cell 33-34: GridSearchCV tuning for SVR
Cell 35:    Evaluate Tuned SVR model
Cell 36-37: Train Random Forest Regression
Cell 38:    Evaluate Random Forest model
Cell 39-40: Compare all models & select best (Random Forest)
Cell 41:    Save best model & scaler to disk
Cell 42:    Save scaler for preprocessing
Cell 43-44: Make predictions on test data
Cell 45:    Visualize predictions vs actual values
```

#### Models Trained (7 Total):
1. **Linear Regression** → R² = 0.9617
2. **Ridge Regression** → R² = 0.9618
3. **Lasso Regression** → R² = 0.9561
4. **ElasticNet** → R² = 0.9577
5. **SVR (baseline)** → R² = 0.9735
6. **SVR (tuned with GridSearchCV)** → R² = 0.9781
7. **Random Forest** → R² = 0.9829 ⭐ **BEST**

#### Key Outputs:
- `best_model.pkl` (Saved Random Forest model)
- `scaler.pkl` (Saved StandardScaler for preprocessing)
- Evaluation metrics for all 7 models
- Prediction visualization plot

#### Model Comparison Results:
```
Model                   R² Score    Status
────────────────────────────────────────────
Random Forest           0.9829      ⭐ Selected
Tuned SVR               0.9781      
SVR                     0.9735      
Ridge Regression        0.9618      
Linear Regression       0.9617      
ElasticNet              0.9577      
Lasso Regression        0.9561      
```

---

## Running the Notebooks

### Prerequisites:
```bash
pip install -r requirements.txt
```

### Sequential Execution:
1. **First Run**: `EDA_Feature_engineering.ipynb`
   - Generates: `cleaned_student_social_media_addiction.csv`

2. **Second Run**: `model_training.ipynb`
   - Uses: `cleaned_student_social_media_addiction.csv`
   - Generates: `best_model.pkl`, `scaler.pkl`

3. **Then Run Flask App**:
   ```bash
   python app.py
   ```

---

## Key Cells to Monitor

### EDA Notebook - Critical Cells:
- Cell with `dataset.info()` → Check data types
- Cell with `cat_cols` → Verify categorical columns
- Cell with `num_cols` → Verify numeric columns
- Cell with `dataset.describe()` → Statistical summary
- Cell with correlation heatmap → Feature relationships

### Model Training Notebook - Critical Cells:
- Cell with model comparison → Verify all models trained
- Cell with `best_model_name` → Confirm Random Forest is best
- Cell saving `best_model.pkl` → Ensure model saved
- Cell saving `scaler.pkl` → Ensure scaler saved

---

## Troubleshooting

### If Notebooks Don't Run:

**Issue**: ModuleNotFoundError
```bash
Solution: pip install -r requirements.txt
```

**Issue**: File not found (CSV)
```bash
Solution: Ensure notebook is in same directory as CSV file
```

**Issue**: Out of Memory
```bash
Solution: Reduce hyperparameters or restart kernel
```

**Issue**: Model not saved
```bash
Solution: Run the save cells explicitly:
joblib.dump(best_model, 'best_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

---

## Expected Notebook Execution Time

- **EDA_Feature_engineering.ipynb**: ~2-3 minutes
- **model_training.ipynb**: ~5-10 minutes (depending on GridSearchCV)
- **Total**: ~10-15 minutes

---

**Last Updated**: December 15, 2025  
**Status**: ✅ Ready for execution
