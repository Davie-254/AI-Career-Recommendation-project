# AI Career Recommendation System for CIT Students

A complete web-based application that uses Machine Learning to recommend suitable career paths for Computer and Information Technology (CIT) students based on their interests, skills, and academic performance.

## 🎯 Project Overview

This system helps CIT students identify suitable career paths from the following options:
- Software Developer
- Network Administrator
- Cybersecurity Specialist
- Data Analyst
- System Administrator

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript (form validation)

### Backend
- Python 3.8+
- Flask framework

### Machine Learning
- Scikit-learn (Decision Tree Classifier)
- Pandas (data processing)
- NumPy (numerical operations)

## 📁 Project Structure

```
career_recommendation_system/
│
├── app.py                      # Flask application (backend)
├── train_model.py              # ML model training script
├── model.pkl                   # Trained model (generated after training)
├── dataset.csv                 # Training dataset (generated after training)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── index.html             # Home page
│   ├── form.html              # Career assessment form
│   └── result.html            # Results page
│
└── static/                     # Static files
    └── style.css              # CSS styling

```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

Open your terminal/command prompt and run:

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install Flask==3.0.0
pip install scikit-learn==1.3.2
pip install pandas==2.1.3
pip install numpy==1.26.2
```

### Step 2: Train the Machine Learning Model

Before running the application, you need to train the ML model:

```bash
python train_model.py
```

This will:
- Create a synthetic dataset (250 samples)
- Train a Decision Tree classifier
- Display model accuracy and evaluation metrics
- Save the trained model as `model.pkl`
- Save the dataset as `dataset.csv`

Expected output:
```
============================================================
Career Recommendation System - Model Training
============================================================

1. Creating dataset...
   Dataset created with 250 samples
   Dataset saved to 'dataset.csv'

2. Dataset Distribution:
Software Developer           50
Network Administrator        50
Cybersecurity Specialist     50
Data Analyst                 50
System Administrator         50

3. Preparing data for training...
   Training samples: 200
   Testing samples: 50

4. Training Decision Tree Classifier...
   Model training completed!

5. Evaluating model...
   Accuracy Score: 95.00%+

...

9. Saving model...
   Model saved as 'model.pkl'

============================================================
Training completed successfully!
============================================================
```

### Step 3: Run the Flask Application

Start the web server:

```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 4: Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

## 📝 How to Use

1. **Home Page**: Click "Start Career Assessment" button
2. **Fill the Form**: 
   - Select your interest levels in Programming, Networking, Cybersecurity, and Data Analysis
   - Rate your Problem-Solving skills
   - Select your Academic Performance level
3. **Get Results**: View your recommended career path with detailed explanation
4. **Try Again**: You can go back and try different inputs

## 🔍 Input Features

The system collects the following information:

| Feature | Options |
|---------|---------|
| Interest in Programming | Low, Medium, High |
| Interest in Networking | Low, Medium, High |
| Interest in Cybersecurity | Low, Medium, High |
| Interest in Data Analysis | Low, Medium, High |
| Problem-Solving Skill Level | Low, Medium, High |
| Academic Performance | Low, Average, High |

## 🎓 Career Output Categories

1. **Software Developer**
   - Strong programming and problem-solving skills
   - Tools: Python, Java, JavaScript, Git

2. **Network Administrator**
   - Strong networking interests
   - Tools: Cisco, Routers, Switches

3. **Cybersecurity Specialist**
   - High cybersecurity interest
   - Tools: Firewalls, Security Scanners

4. **Data Analyst**
   - Strong data analysis interest
   - Tools: Python, SQL, Tableau, Power BI

5. **System Administrator**
   - Balanced technical skills
   - Tools: Linux, Windows Server, VMware

## 📊 Model Performance

The Decision Tree classifier achieves:
- **Accuracy**: 95%+ on test data
- **Training/Test Split**: 80/20
- **Dataset Size**: 250 samples (50 per career)
- **Features**: 6 input features

## 🔧 Troubleshooting

### Issue: "Model not loaded" error
**Solution**: Run `python train_model.py` first to create the model file

### Issue: "Module not found" error
**Solution**: Install missing dependencies using `pip install -r requirements.txt`

### Issue: Port 5000 already in use
**Solution**: Change port in app.py: `app.run(debug=True, port=5001)`

### Issue: Page not loading
**Solution**: 
- Ensure Flask is running
- Check the terminal for error messages
- Try http://127.0.0.1:5000 instead of localhost

## 🎨 Features

- ✅ Clean and modern UI design
- ✅ Responsive layout (mobile-friendly)
- ✅ Client-side form validation
- ✅ Real-time prediction using ML model
- ✅ Detailed career explanations
- ✅ Confidence score display
- ✅ Print-friendly results page
- ✅ Easy navigation

## 📚 Learning Outcomes

This project demonstrates:
- Full-stack web development
- Machine Learning integration
- RESTful API design
- Form handling and validation
- Data preprocessing
- Model training and evaluation
- User interface design

## 🔮 Future Enhancements

Potential improvements:
- Database integration for storing user responses
- More career categories
- Personalized learning path recommendations
- Export results as PDF
- User authentication
- Career comparison feature
- Industry trends integration

## 📧 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section
2. Review the terminal output for error messages
3. Ensure all dependencies are installed correctly

## 📄 License

This project is created for educational purposes.

---

**Created**: 2024  
**Version**: 1.0  
**Technology Stack**: Python, Flask, Scikit-learn, HTML, CSS, JavaScript
