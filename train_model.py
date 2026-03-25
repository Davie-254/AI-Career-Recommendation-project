"""
Career Recommendation System - Model Training Script
This script creates a dataset, trains a Decision Tree classifier, and saves the model
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Create synthetic dataset for training
def create_dataset():
    """
    Create a structured dataset with features and career labels
    Features: Programming, Networking, Cybersecurity, Data Analysis, Problem Solving, Academic Performance
    Labels: Software Developer, Network Administrator, Cybersecurity Specialist, Data Analyst, System Administrator
    """
    
    np.random.seed(42)
    
    data = []
    
    # Software Developer profiles (strong programming, good problem solving)
    for _ in range(50):
        data.append([
            np.random.choice([2, 3]),  # High programming
            np.random.choice([1, 2]),  # Low-Medium networking
            np.random.choice([1, 2]),  # Low-Medium cybersecurity
            np.random.choice([1, 2, 3]),  # Varied data analysis
            np.random.choice([2, 3]),  # High problem solving
            np.random.choice([2, 3]),  # Average-High academic
            'Software Developer'
        ])
    
    # Network Administrator profiles (strong networking)
    for _ in range(50):
        data.append([
            np.random.choice([1, 2]),  # Low-Medium programming
            np.random.choice([2, 3]),  # High networking
            np.random.choice([2, 3]),  # Medium-High cybersecurity
            np.random.choice([1, 2]),  # Low-Medium data analysis
            np.random.choice([2, 3]),  # Medium-High problem solving
            np.random.choice([2, 3]),  # Average-High academic
            'Network Administrator'
        ])
    
    # Cybersecurity Specialist profiles (strong cybersecurity and networking)
    for _ in range(50):
        data.append([
            np.random.choice([2, 3]),  # Medium-High programming
            np.random.choice([2, 3]),  # High networking
            np.random.choice([3]),  # High cybersecurity
            np.random.choice([1, 2]),  # Low-Medium data analysis
            np.random.choice([3]),  # High problem solving
            np.random.choice([2, 3]),  # Average-High academic
            'Cybersecurity Specialist'
        ])
    
    # Data Analyst profiles (strong data analysis)
    for _ in range(50):
        data.append([
            np.random.choice([2, 3]),  # Medium-High programming
            np.random.choice([1, 2]),  # Low-Medium networking
            np.random.choice([1, 2]),  # Low-Medium cybersecurity
            np.random.choice([3]),  # High data analysis
            np.random.choice([2, 3]),  # Medium-High problem solving
            np.random.choice([2, 3]),  # Average-High academic
            'Data Analyst'
        ])
    
    # System Administrator profiles (balanced technical skills)
    for _ in range(50):
        data.append([
            np.random.choice([2, 3]),  # Medium-High programming
            np.random.choice([2, 3]),  # High networking
            np.random.choice([2, 3]),  # Medium-High cybersecurity
            np.random.choice([1, 2]),  # Low-Medium data analysis
            np.random.choice([2, 3]),  # Medium-High problem solving
            np.random.choice([2, 3]),  # Average-High academic
            'System Administrator'
        ])
    
    # Create DataFrame
    columns = ['Programming', 'Networking', 'Cybersecurity', 'DataAnalysis', 
            'ProblemSolving', 'Academic', 'Career']
    df = pd.DataFrame(data, columns=columns)
    
    return df

# Main training function
def train_and_save_model():
    print("=" * 60)
    print("Career Recommendation System - Model Training")
    print("=" * 60)
    
    # Create dataset
    print("\n1. Creating dataset...")
    df = create_dataset()
    
    # Save dataset to CSV
    df.to_csv('dataset.csv', index=False)
    print(f"   Dataset created with {len(df)} samples")
    print(f"   Dataset saved to 'dataset.csv'")
    
    # Display dataset info
    print("\n2. Dataset Distribution:")
    print(df['Career'].value_counts())
    
    # Prepare features and labels
    print("\n3. Preparing data for training...")
    X = df.drop('Career', axis=1)
    y = df['Career']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"   Training samples: {len(X_train)}")
    print(f"   Testing samples: {len(X_test)}")
    
    # Train Decision Tree model
    print("\n4. Training Decision Tree Classifier...")
    model = DecisionTreeClassifier(
        criterion='gini',
        max_depth=10,
        min_samples_split=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    print("   Model training completed!")
    
    # Make predictions
    print("\n5. Evaluating model...")
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"   Accuracy Score: {accuracy * 100:.2f}%")
    
    # Display confusion matrix
    print("\n6. Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    print(cm)
    
    # Display classification report
    print("\n7. Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature importance
    print("\n8. Feature Importance:")
    feature_names = X.columns
    importances = model.feature_importances_
    for name, importance in zip(feature_names, importances):
        print(f"   {name}: {importance:.4f}")
    
    # Save model
    print("\n9. Saving model...")
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("   Model saved as 'model.pkl'")
    
    print("\n" + "=" * 60)
    print("Training completed successfully!")
    print("=" * 60)
    
    return model

if __name__ == "__main__":
    train_and_save_model()
