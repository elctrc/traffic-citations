import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('make_model.pkl', 'rb'))

@app.route('/api', methods=['POST'])

def predict():
    # Get data from POST request
    data = request.get_json(force=True)
    # Make prediction from loaded model
    prediction = model.predict([[np.array(data['exp'])]])
    # Get first value of prediction
    output = prediction[0]
    return jsonify(output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)