# traffic-citations
Contains corrupted data set of vehicle citations. The goal of this project is to predict the make of each missing vehicle

## Installation
Install method described uses virtualenv:
* Clone this repo into your local environment
* CD into the repo
* Install virtualenv if not already installed: `pip install virtualenv`
* Create new virtualenv using Python 3: `virtualenv --python=python3.7 venv` (example)
* Activate virtualenv: `source venv/bin/activate`
* Install from requirements: `pip install -r requirements.txt`

## To Run
* Update `test_features.py` with the values you wish to send
* Run `run.sh`, which will begin the server with a pre-trained model
* Run `request.py` in a new terminal window
* The request will return a prediction in the form of "Prediction: {Make}", along with letting you know if it's in the top 25 Makes
* If you wish to re-train the model and start the server you can use `run_model.sh` instead
* Lastly, just to show it can return a different result: You can copy over the data from `test_features_alternate.py` (or just change the name) and re-run.

## Known Issues
* I have noticed that on occasion I will need to restart my terminal in order to get the request to work properly. If it seems to be hanging at "Sending request..." then restart your terminal and run `run.sh` once more.

## Exploratory Data Analysis
* EDA can be found in the `notebooks\traffic_incidents.ipynb` Jupyter notebook.

## Notes on the model itself
This is by no means a good model! It is a very basic Random Forest Classifier - and the features ultimately chosen were for expediency sake (to avoid making dummies). Given the fact that I experimented with many features and was not able to break 20% accuracy it seemed worth it to just plow ahead to get it deployed and if I had time I would get back to making it better.

## Model Feasibility
At the moment, this model does not seem like a viable solution. I attempted to choose various features and re-run the model, but was never able to break even 20% accuracy. It could be that there is simply not enough relevant information in the chosen features to make an accurate prediction of the Make of a vehicle. Given more time, I would attempt to run NLP on some of the text columns (Location, Violation Description) to see if there might be some correlation there.