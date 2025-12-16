# 🎯 QUICK START GUIDE - Social Media Addiction Detector

## ⚡ 5-Minute Setup

### Step 1: Install Dependencies (1 min)
```bash
cd c:\tareq\python\Student-Socail-media-addiction
pip install -r requirements.txt
```

### Step 2: Run Notebooks (5 min - First Time Only)
```
1. Open: Notebooks/EDA_Feature_engineering.ipynb
2. Run All Cells (Ctrl+Shift+Enter)
3. Open: Notebooks/model_training.ipynb
4. Run All Cells (Ctrl+Shift+Enter)
```

### Step 3: Start Flask App (1 min)
```bash
python app.py
```

### Step 4: Open Web Application
```
Browser: http://localhost:5000
```

---

## 📱 Using the Application

### Fill the Form:
1. **Gender**: Select Male/Female/Other
2. **Academic Level**: Select education level
3. **Country**: Select your country
4. **Daily Usage**: Slide to select hours (0-24)
5. **Sleep Quality**: Rate your sleep (1-10)
6. **Social Anxiety**: Rate anxiety level (1-10)
7. **Self-Esteem**: Rate self-esteem (1-10)
8. **Motivation Loss**: Rate motivation loss (1-10)

### Get Results:
- 🟢 **Green (0-25)**: Low addiction - Healthy usage!
- 🟡 **Yellow (25-50)**: Moderate - Consider reducing time
- 🟠 **Orange (50-75)**: High - Seek professional help
- 🔴 **Red (75-100)**: Severe - Professional help recommended

---

## 📊 Project Overview

### Files You Need:
- ✅ `app.py` - Flask web server
- ✅ `templates/index.html` - Web interface
- ✅ `best_model.pkl` - AI model (auto-generated)
- ✅ `scaler.pkl` - Data preprocessor (auto-generated)
- ✅ `requirements.txt` - Dependencies

### What It Does:
1. Takes your inputs (8 features)
2. Encodes categorical values
3. Scales numeric values
4. Runs Random Forest ML model
5. Predicts addiction score (0-100)
6. Classifies into 4 levels
7. Shows personalized advice

### Model Performance:
- **Accuracy**: 98.29% (R² = 0.9829)
- **Type**: Random Forest Regressor
- **Training Data**: 1054 students
- **Features Used**: 8

---

## 🔧 Troubleshooting

### Problem: "best_model.pkl not found"
**Solution**: Run `model_training.ipynb` notebook

### Problem: Port 5000 already in use
**Solution**: Edit app.py line, change `port=5000` to `port=5001`

### Problem: ModuleNotFoundError
**Solution**: Run `pip install -r requirements.txt`

### Problem: Form not working
**Solution**: Check browser console (F12) for errors

---

## 📂 File Structure

```
Student-Socail-media-addiction/
├── Notebooks/
│   ├── EDA_Feature_engineering.ipynb (run first)
│   ├── model_training.ipynb (run second)
│   └── *.csv files
├── templates/
│   └── index.html (web interface)
├── app.py (main server)
├── best_model.pkl (auto-generated)
├── scaler.pkl (auto-generated)
└── requirements.txt
```

---

## 💡 Key Information

### Input Features (8 Total):
1. Gender (Male/Female/Other)
2. Academic Level (High School/Bachelor/Master/PhD)
3. Country (9 options)
4. Daily Usage Hours (0-24)
5. Sleep Quality (1-10)
6. Social Anxiety (1-10)
7. Self-Esteem (1-10)
8. Motivation Loss (1-10)

### Output:
- **Score**: 0-100 addiction level
- **Classification**: Low/Moderate/High/Severe
- **Recommendation**: Personalized advice

---

## 🎓 Documentation Files

For more detailed information, see:
- `PROJECT_COMPLETION.md` - Full checklist
- `ARCHITECTURE.md` - Data flow diagrams
- `NOTEBOOKS_GUIDE.md` - Notebook details
- `PROJECT_REVIEW.md` - Complete overview
- `FLASK_README.md` - Flask documentation

---

## ⚙️ System Requirements

- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Disk**: 500MB free space
- **Browser**: Any modern browser

---

## 🚀 Production Deployment

Ready to deploy? The app is production-ready!

Next steps:
1. Use WSGI server (Gunicorn)
2. Add SSL certificate
3. Deploy to cloud (AWS/Azure/Heroku)
4. Set up monitoring

---

## 📞 Support

**All documentation is in the project folder:**
- Questions about notebooks? → `NOTEBOOKS_GUIDE.md`
- Questions about architecture? → `ARCHITECTURE.md`
- Questions about Flask app? → `FLASK_README.md`
- Questions about project? → `PROJECT_REVIEW.md`

---

**Status**: ✅ READY TO USE  
**Last Updated**: December 15, 2025
