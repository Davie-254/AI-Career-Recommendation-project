# 📐 SYSTEM ARCHITECTURE & FLOW DIAGRAM

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   USER INTERFACE (Browser)                      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  Home Page   │  │  Form Page   │  │ Result Page  │        │
│  │  index.html  │  │  form.html   │  │ result.html  │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
│         │                 │                  │                  │
│         └─────────────────┴──────────────────┘                  │
│                          │                                       │
└──────────────────────────┼───────────────────────────────────────┘
                           │
                    HTTP Request/Response
                           │
┌──────────────────────────┼───────────────────────────────────────┐
│                  FLASK WEB SERVER (app.py)                       │
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌──────────────┐       │
│  │   Routes    │────│  Controllers │────│   Handlers   │       │
│  │  @app.route │    │    Logic     │    │  Form Data   │       │
│  └─────────────┘    └─────────────┘    └──────────────┘       │
│         │                  │                   │                 │
│         └──────────────────┴───────────────────┘                 │
│                            │                                     │
└────────────────────────────┼─────────────────────────────────────┘
                             │
                      Data Processing
                             │
┌────────────────────────────┼─────────────────────────────────────┐
│             MACHINE LEARNING LAYER                               │
│                                                                  │
│  ┌──────────────────┐                                           │
│  │   model.pkl      │  (Trained Decision Tree Model)           │
│  │   - Load Model   │                                           │
│  │   - Predict      │                                           │
│  │   - Get Results  │                                           │
│  └──────────────────┘                                           │
│         │                                                        │
│         │ Input: [Programming, Networking, Cybersecurity,       │
│         │         DataAnalysis, ProblemSolving, Academic]       │
│         │                                                        │
│         │ Output: Career Recommendation                         │
│         │                                                        │
└─────────┼──────────────────────────────────────────────────────┘
          │
    Prediction Result
          │
┌─────────┼──────────────────────────────────────────────────────┐
│      PRESENTATION LAYER                                          │
│                                                                  │
│  ┌────────────────────────────────────────────────┐            │
│  │  Render Template with:                          │            │
│  │  - Career Name                                  │            │
│  │  - Description                                  │            │
│  │  - Explanation                                  │            │
│  │  - Skills Required                              │            │
│  │  - Tools & Technologies                         │            │
│  │  - Confidence Score                             │            │
│  └────────────────────────────────────────────────┘            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌──────────┐
│  START   │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│  User Opens     │
│  Home Page      │
│  (index.html)   │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Click Start    │
│  Assessment     │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Load Form Page │
│  (form.html)    │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  User Fills     │
│  6 Input Fields │
│  - Programming  │
│  - Networking   │
│  - Cybersecurity│
│  - Data Analysis│
│  - Problem      │
│  - Academic     │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  Form           │
│  Validation     │
│  (JavaScript)   │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│  POST Request   │
│  to /predict    │
└────┬────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  Flask Backend                   │
│  1. Receive form data            │
│  2. Convert to numerical values  │
│     Low = 1, Medium = 2, High = 3│
│  3. Create feature array         │
│     [3, 1, 2, 2, 3, 3]          │
└────┬─────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  Load ML Model                   │
│  (model.pkl)                     │
│  - Decision Tree Classifier      │
└────┬─────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  Model Prediction                │
│  - Input: Feature Array          │
│  - Process: Decision Tree Logic  │
│  - Output: Career Category       │
│  - Confidence: Probability Score │
└────┬─────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  Retrieve Career Information     │
│  - Description                   │
│  - Explanation                   │
│  - Required Skills               │
│  - Tools & Technologies          │
└────┬─────────────────────────────┘
     │
     ▼
┌─────────────────────────────────┐
│  Render Result Page              │
│  (result.html)                   │
│  - Display Career                │
│  - Show Details                  │
│  - Present Options               │
└────┬─────────────────────────────┘
     │
     ▼
┌─────────────────┐
│  User Reviews   │
│  Results        │
└────┬────────────┘
     │
     ├───────────────┐
     │               │
     ▼               ▼
┌─────────┐    ┌─────────┐
│ Try     │    │ Go Back │
│ Again   │    │ to Home │
└─────────┘    └─────────┘
```

---

## Model Training Flow

```
┌──────────────┐
│  START       │
│  Training    │
└──────┬───────┘
       │
       ▼
┌───────────────────────────────┐
│  Create Synthetic Dataset      │
│  - 250 samples total           │
│  - 50 samples per career       │
│  - 6 features per sample       │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Define Career Profiles        │
│  Software Dev: High Prog       │
│  Network Admin: High Network   │
│  Cybersec: High Security       │
│  Data Analyst: High Data       │
│  Sys Admin: Balanced           │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Save Dataset                  │
│  (dataset.csv)                 │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Split Data                    │
│  - Training: 80% (200 samples) │
│  - Testing: 20% (50 samples)   │
│  - Stratified by career        │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Initialize Model              │
│  - Algorithm: Decision Tree    │
│  - Criterion: Gini            │
│  - Max Depth: 10              │
│  - Min Samples Split: 5       │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Train Model                   │
│  - Fit on training data        │
│  - Learn decision boundaries   │
│  - Create decision tree        │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Evaluate Model                │
│  - Predict on test data        │
│  - Calculate accuracy          │
│  - Generate confusion matrix   │
│  - Print classification report │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Analyze Feature Importance    │
│  - Rank features              │
│  - Display contribution       │
└──────┬────────────────────────┘
       │
       ▼
┌───────────────────────────────┐
│  Save Trained Model            │
│  - Serialize with Pickle       │
│  - Save as model.pkl          │
└──────┬────────────────────────┘
       │
       ▼
┌──────────────┐
│  Training    │
│  Complete    │
└──────────────┘
```

---

## Component Interaction

```
┌─────────────────────────────────────────────────────────────┐
│                      Component Layer                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐        ┌──────────────┐                  │
│  │   Frontend   │◄──────►│   Backend    │                  │
│  │              │  HTTP  │              │                  │
│  │  - HTML      │        │  - Flask     │                  │
│  │  - CSS       │        │  - Routes    │                  │
│  │  - JavaScript│        │  - Logic     │                  │
│  └──────────────┘        └──────┬───────┘                  │
│                                  │                          │
│                                  │ Loads                    │
│                                  ▼                          │
│                         ┌──────────────┐                    │
│                         │   ML Model   │                    │
│                         │              │                    │
│                         │  - model.pkl │                    │
│                         │  - Predict   │                    │
│                         └──────────────┘                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                        Data Layer                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐        ┌──────────────┐                  │
│  │  dataset.csv │        │ Career Info  │                  │
│  │              │        │  Dictionary  │                  │
│  │  Training    │        │              │                  │
│  │  Data        │        │  Hardcoded   │                  │
│  └──────────────┘        └──────────────┘                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Templates   │  │    Static    │  │   Results    │     │
│  │              │  │              │  │              │     │
│  │  - Jinja2    │  │  - CSS       │  │  - Dynamic   │     │
│  │  - HTML      │  │  - Assets    │  │  - Formatted │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Request/Response Cycle

```
USER ACTION                    SERVER PROCESSING               RESPONSE

┌─────────────┐
│ Visit Home  │
└──────┬──────┘
       │ GET /
       ▼
       ┌──────────────┐
       │ Flask Route  │──► Render index.html ──► Display Home
       └──────────────┘

┌─────────────┐
│ Click Start │
└──────┬──────┘
       │ GET /form
       ▼
       ┌──────────────┐
       │ Flask Route  │──► Render form.html ──► Display Form
       └──────────────┘

┌─────────────┐
│ Submit Form │
└──────┬──────┘
       │ POST /predict
       │ Data: {programming: 'High', ...}
       ▼
       ┌──────────────────────────────┐
       │ Flask Route                   │
       │ 1. Get form data             │
       │ 2. Convert to numbers        │
       │ 3. Load model                │
       │ 4. Make prediction           │
       │ 5. Get career info           │
       └──────┬───────────────────────┘
              ▼
       ┌──────────────┐
       │ Render       │──► Display Result Page
       │ result.html  │    with Career Info
       └──────────────┘
```

---

## Technology Stack Layers

```
┌────────────────────────────────────────────────┐
│         Presentation Layer (Frontend)          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   HTML5  │  │   CSS3   │  │JavaScript│    │
│  └──────────┘  └──────────┘  └──────────┘    │
└────────────────────────────────────────────────┘
                      │
┌────────────────────────────────────────────────┐
│          Application Layer (Backend)           │
│  ┌────────────────────────────────────────┐   │
│  │           Flask Framework              │   │
│  │  - Routes  - Controllers  - Handlers   │   │
│  └────────────────────────────────────────┘   │
└────────────────────────────────────────────────┘
                      │
┌────────────────────────────────────────────────┐
│         Business Logic Layer (ML)              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │Scikit-   │  │ Pandas   │  │  NumPy   │    │
│  │ Learn    │  └──────────┘  └──────────┘    │
│  │Decision  │                                 │
│  │Tree      │                                 │
│  └──────────┘                                 │
└────────────────────────────────────────────────┘
                      │
┌────────────────────────────────────────────────┐
│            Data Layer (Storage)                │
│  ┌──────────┐  ┌──────────┐                   │
│  │model.pkl │  │dataset   │                   │
│  │          │  │.csv      │                   │
│  └──────────┘  └──────────┘                   │
└────────────────────────────────────────────────┘
```

---

## File Dependencies

```
app.py
  │
  ├─── Requires: Flask, pickle, numpy
  ├─── Loads: model.pkl
  └─── Uses: templates/*.html, static/style.css

train_model.py
  │
  ├─── Requires: pandas, numpy, sklearn, pickle
  ├─── Creates: model.pkl, dataset.csv
  └─── Output: Trained model

templates/
  │
  ├─── index.html ──► Requires: static/style.css
  ├─── form.html ──► Requires: static/style.css
  └─── result.html ──► Requires: static/style.css

static/
  │
  └─── style.css ──► Used by: all HTML templates

model.pkl
  │
  └─── Used by: app.py (for predictions)

dataset.csv
  │
  └─── Created by: train_model.py
```

---

## Decision Tree Structure (Simplified)

```
                    [Root Node]
                  Programming Interest?
                    /           \
                High               Low/Medium
                /                       \
        Data Analysis?            Networking?
           /      \                 /        \
       High      Low/Med        High       Low/Med
         |          |             |           |
    Data       Cybersec?    Network    Software
    Analyst       /  \        Admin      Dev
              High   Low
               |      |
          Cybersec  System
          Spec.     Admin
```

---

## System States

```
┌─────────────┐
│   IDLE      │ ──► User hasn't started
└─────────────┘

┌─────────────┐
│  INPUTTING  │ ──► User filling form
└─────────────┘

┌─────────────┐
│ PROCESSING  │ ──► Model making prediction
└─────────────┘

┌─────────────┐
│ DISPLAYING  │ ──► Showing results
└─────────────┘

┌─────────────┐
│   RESET     │ ──► User starts new assessment
└─────────────┘
```

---

**End of Architecture Diagram**
