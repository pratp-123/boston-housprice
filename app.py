import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, app, jsonify,render_template

app = Flask(__name__)

with open('regmodel.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaling.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    print(data)
    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    prediction = model.predict(new_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
