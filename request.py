import argparse
import requests

url = 'http://localhost:5000/api'

parser = argparse.ArgumentParser()
parser.add_argument('features', help='A json formatted file object of features')
args = parser.parse_args()
features = args.features
print(features)

r = requests.post(url, json=features)
# r = requests.post(url, json={'exp':1.8})
print(r.json())