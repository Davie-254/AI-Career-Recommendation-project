"""
Career Recommendation System - Flask Application
Main backend file that handles routing and predictions
"""

from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    print("❌ ERROR: model.pkl not found. Please run train_model.py first!")
    model = None

# Mapping dictionaries
INTEREST_MAPPING = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

# Updated Academic Mapping for Percentage-based System
ACADEMIC_MAPPING = {
    'Pass': 1,           # 40% to 59%
    'Second Class': 2,   # 60% to 69%
    'First Class': 3     # 70% and above
}

# Career explanations
CAREER_EXPLANATIONS = {
    'Software Developer': {
        'description': 'You are recommended for a Software Developer role!',
        'explanation': 'Based on your strong programming interests and problem-solving skills, you would excel in developing applications, writing code, and creating software solutions. This career involves designing, testing, and maintaining software systems.',
        'skills': 'Programming, Problem-Solving, Logical Thinking',
        'tools': 'Python, Java, C++, JavaScript, Git, IDEs'
    },
    'Network Administrator': {
        'description': 'You are recommended for a Network Administrator role!',
        'explanation': 'Your strong networking interests and technical skills make you ideal for managing and maintaining computer networks. This career involves configuring network hardware, troubleshooting connectivity issues, and ensuring network security and performance.',
        'skills': 'Networking, System Configuration, Troubleshooting',
        'tools': 'Cisco, Routers, Switches, Network Monitoring Tools'
    },
    'Cybersecurity Specialist': {
        'description': 'You are recommended for a Cybersecurity Specialist role!',
        'explanation': 'Your high interest in cybersecurity combined with strong problem-solving abilities makes you perfect for protecting systems and data from cyber threats. This career involves identifying vulnerabilities, implementing security measures, and responding to security incidents.',
        'skills': 'Security Analysis, Risk Assessment, Ethical Hacking',
        'tools': 'Firewalls, IDS/IPS, Security Scanners, Penetration Testing Tools'
    },
    'Data Analyst': {
        'description': 'You are recommended for a Data Analyst role!',
        'explanation': 'Your strong interest in data analysis and analytical skills make you well-suited for interpreting complex datasets and providing insights. This career involves collecting, processing, and analyzing data to help organizations make informed decisions.',
        'skills': 'Data Analysis, Statistical Thinking, Data Visualization',
        'tools': 'Python, R, SQL, Excel, Tableau, Power BI'
    },
    'System Administrator': {
        'description': 'You are recommended for a System Administrator role!',
        'explanation': 'Your balanced technical skills across multiple areas make you ideal for maintaining and managing IT infrastructure. This career involves installing, configuring, and maintaining servers, managing user accounts, and ensuring system reliability.',
        'skills': 'System Management, Server Administration, Troubleshooting',
        'tools': 'Linux, Windows Server, VMware, Active Directory, Scripting'
    }
}

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/form')
def form():
    """Career input form page route"""
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle form submission and make prediction"""
    
    print("\n" + "="*60)
    print("📋 PREDICTION REQUEST RECEIVED")
    print("="*60)
    
    if model is None:
        print("❌ ERROR: Model is None!")
        return render_template('result.html', 
                            error="Model not loaded. Please run: python train_model.py",
                            career=None)
    
    try:
        # Get form data
        print("\n1️⃣ Getting form data...")
        programming = request.form.get('programming')
        networking = request.form.get('networking')
        cybersecurity = request.form.get('cybersecurity')
        data_analysis = request.form.get('data_analysis')
        problem_solving = request.form.get('problem_solving')
        academic = request.form.get('academic')
        
        print(f"   Programming: {programming}")
        print(f"   Networking: {networking}")
        print(f"   Cybersecurity: {cybersecurity}")
        print(f"   Data Analysis: {data_analysis}")
        print(f"   Problem Solving: {problem_solving}")
        print(f"   Academic: {academic}")
        
        # Validate all fields are filled
        if not all([programming, networking, cybersecurity, data_analysis, problem_solving, academic]):
            print("❌ ERROR: Some fields are missing!")
            return render_template('result.html',
                                error="Please fill in all fields in the form.",
                                career=None)
        
        # Convert to numerical values
        print("\n2️⃣ Converting to numerical values...")
        features = [
            INTEREST_MAPPING[programming],
            INTEREST_MAPPING[networking],
            INTEREST_MAPPING[cybersecurity],
            INTEREST_MAPPING[data_analysis],
            INTEREST_MAPPING[problem_solving],
            ACADEMIC_MAPPING[academic]
        ]
        print(f"   Features: {features}")
        
        # Make prediction
        print("\n3️⃣ Making prediction...")
        features_array = np.array([features])
        prediction = model.predict(features_array)[0]
        print(f"   ✅ Prediction: {prediction}")
        
        # Get probability scores
        probabilities = model.predict_proba(features_array)[0]
        confidence = max(probabilities) * 100
        print(f"   📊 Confidence: {confidence:.1f}%")
        
        # Get career information
        career_info = CAREER_EXPLANATIONS[prediction]
        
        print("\n4️⃣ Rendering result page...")
        print("="*60 + "\n")
        
        return render_template('result.html',
                            career=prediction,
                            description=career_info['description'],
                            explanation=career_info['explanation'],
                            skills=career_info['skills'],
                            tools=career_info['tools'],
                            confidence=f"{confidence:.1f}",
                            error=None)
    
    except KeyError as e:
        print(f"\n❌ KEY ERROR: {str(e)}")
        print("This usually means the form value doesn't match the mapping.")
        import traceback
        traceback.print_exc()
        print("="*60 + "\n")
        
        return render_template('result.html',
                            error=f"Invalid form value: {str(e)}. Please check your selections.",
                            career=None)
    
    except Exception as e:
        print(f"\n❌ ERROR OCCURRED: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        print("="*60 + "\n")
        
        return render_template('result.html',
                            error=f"An error occurred: {str(e)}",
                            career=None)

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Starting Career Recommendation System")
    print("="*60)
    print("📍 Server will run at: http://127.0.0.1:5000")
    print("📍 Or: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)
