from flask import Flask, render_template, request
import pickle
import numpy as np
import sqlite3

app = Flask(__name__)
model = pickle.load(open("wine_quality_model.pkl", "rb"))

# Initialize DB
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    features TEXT,
                    predicted_quality REAL)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    inputs = [float(x) for x in request.form.values()]
    prediction = model.predict(np.array(inputs).reshape(1, -1))[0]

    cursor.execute("INSERT INTO predictions (features, predicted_quality) VALUES (?, ?)",
                   (str(inputs), prediction))
    conn.commit()
    
    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)