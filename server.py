import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('make_model.pkl', 'rb'))

@app.route('/api', methods=['POST'])

def predict():
    # Get data from POST request
    print(' * Getting request...')
    # data = request.get_json(force=True)
    data = request.get_json()
    # Convert dict to dataframe
    df = pd.DataFrame(data, index = [0])
    # Make prediction from loaded model
    print(' * Making prediction...')
    prediction = model.predict(df)
    # Get first value of prediction
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)