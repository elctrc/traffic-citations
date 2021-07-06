from test_features import features
import pickle
import requests

url = 'http://localhost:5000/api'

# Load up our top 25 Makes
top_25 = pickle.load(open('top_25.pkl', 'rb'))

print('Sending request...')
r = requests.post(url, json=features)

pred = r.json()
print('Prediction:', pred) 
if pred in top_25:
    print("And it's in the top 25!")