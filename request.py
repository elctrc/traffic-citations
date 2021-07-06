from test_features import features
import requests

url = 'http://localhost:5000/api'

print('Sending request...')
r = requests.post(url, json=features)
# r = requests.post(url, json=features)
# r = requests.post(url, json={'exp':1.8})
print('Prediction:', r.json()) 