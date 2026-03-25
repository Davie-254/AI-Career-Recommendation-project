# 🚀 QUICK START GUIDE

## Run the Project in 3 Steps

### Step 1: Install Dependencies
```bash
pip install Flask scikit-learn pandas numpy
```

### Step 2: Train the Model
```bash
python train_model.py
```
Wait for "Training completed successfully!" message

### Step 3: Start the Application
```bash
python app.py
```

### Step 4: Open in Browser
Open: http://localhost:5000

---

## That's it! You're ready to use the system.

### Testing the System

Try these example inputs for different career recommendations:

#### Software Developer
- Programming: High
- Networking: Low
- Cybersecurity: Medium
- Data Analysis: Medium
- Problem Solving: High
- Academic: High

#### Network Administrator
- Programming: Medium
- Networking: High
- Cybersecurity: High
- Data Analysis: Low
- Problem Solving: High
- Academic: Average

#### Cybersecurity Specialist
- Programming: High
- Networking: High
- Cybersecurity: High
- Data Analysis: Low
- Problem Solving: High
- Academic: High

#### Data Analyst
- Programming: Medium
- Networking: Low
- Cybersecurity: Low
- Data Analysis: High
- Problem Solving: High
- Academic: High

#### System Administrator
- Programming: High
- Networking: High
- Cybersecurity: Medium
- Data Analysis: Low
- Problem Solving: High
- Academic: Average

---

## Common Commands

Stop the server: `Ctrl + C`

Retrain model: `python train_model.py`

Change port: Edit `app.py`, change `port=5000` to desired port

---

## File Checklist

Before running, ensure you have:
- ✅ train_model.py
- ✅ app.py
- ✅ requirements.txt
- ✅ templates/index.html
- ✅ templates/form.html
- ✅ templates/result.html
- ✅ static/style.css

After training, you'll also have:
- ✅ model.pkl (created by training)
- ✅ dataset.csv (created by training)

---

## Need Help?

Check README.md for detailed documentation and troubleshooting.
