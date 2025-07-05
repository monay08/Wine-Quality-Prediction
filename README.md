### 🍷 Wine Quality Prediction Web App

This project is a simple web application that predicts the quality of wine based on its physicochemical properties using Machine Learning.

It combines:
- A machine learning model (Random Forest Regressor)
- A Flask web application
- SQLite database to store predictions

## 📂 Dataset
The dataset used is from the UCI Machine Learning Repository via Kaggle:
[Wine Quality Dataset (Red Wine)](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

## 🚀 Features
- Predicts wine quality score based on chemical properties.
- Simple and clean web interface using Flask and Bootstrap.
- Saves every prediction with input features into SQLite database.
- Ready for local deployment and further extension.

## 🛠️ Tech Stack
- Python
- Flask
- scikit-learn
- pandas
- numpy
- SQLite
- Bootstrap (for UI)

## 📋 Project Structure
wine_quality_app/
│
├── app.py # Flask Web App
├── wine_quality_model.pkl # Trained Machine Learning Model
├── winequality-red.csv # Dataset
├── database.db # SQLite Database (Auto-created)
├── requirements.txt # Dependencies
│
├── templates/ # HTML Templates
│ ├── index.html # Input Form Page
│ └── result.html # Result Page
│
└── static/ # (Optional) CSS, JS, Images

## ⚙️ How to Run Locally
1. **Clone this repository:**
git clone https://github.com/monay08/Wine-Quality-Prediction.git
cd Wine-Quality-Prediction

2. **Install dependencies:**
pip install -r requirements.txt

3. **Download the Dataset:**
Download the dataset from Kaggle and place winequality-red.csv in the project folder.

4. **Run the Flask Web App:**
python app.py

5. **Open the App:**
Visit http://127.0.0.1:5000/ in your browser.


👩‍💻 Author
Daisy Lou Montante
GitHub: @monay08

Note: This project was created for educational purposes and class presentations.