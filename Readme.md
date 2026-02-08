# 🌸 ML Project – Iris Classification (Streamlit + SVM)

## 📌 Project Overview
This project is a **Machine Learning web application** built using **Python, Scikit-learn, and Streamlit**.  
It predicts the **species of Iris flower** based on input features using a trained **Support Vector Machine (SVM)** model.

---

## 🚀 Features
- Trained ML model using Iris dataset  
- Streamlit web interface  
- Real-time prediction  
- Simple and clean UI  
- Pre-trained model loading using pickle  

---

## 🗂️ Project Structure
cat > README.md << 'EOF'
ML_project/
│
├── app.py                # Streamlit web app
├── model_train.ipynb     # Model training notebook
├── IRIS.csv              # Dataset
├── SVM.pkl               # Trained ML model
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── venv/                 # Virtual environment (optional)
EOF
---

## 🧠 Machine Learning Model
- **Algorithm:** Support Vector Machine (SVM)  
- **Dataset:** Iris Dataset  

### Features Used
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone <your-repo-link>
cd ML_project

### 2️⃣ Create Virtual Environment And Run (Optional but Recommended)

python -m venv venv

Activate Environment:

Linux / Mac
source venv/bin/activate


Windows
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶️ Run the Application

streamlit run app.py

Open in browser:

http://localhost:8501

---

## 📊 Model Training

If you want to retrain the model:

Open model_train.ipynb

Run all cells

New model will be saved as .pkl

---

## 🛠️ Technologies Used

Python

Scikit-learn

Streamlit

Pandas

NumPy

Pickle

---

## 📌 Future Improvements

Add more ML models

Improve UI design

Deploy on cloud (Streamlit Cloud / AWS / Render)

Add model accuracy comparison

---

## 👨‍💻 Author

Asif Hussain Tahiri

---

## 📜 License

This project is for educational purposes.


