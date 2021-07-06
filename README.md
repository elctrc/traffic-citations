# traffic-citations
Contains corrupted data set of vehicle citations. The goal of this project is to predict the make of each missing vehicle

## To Run
* Run `run.sh`, which will begin the server with a pre-trained model.
* If you wish to re-train the model and start the server you can use `run_model.sh` instead

Currently, the model will run and store the data. The server will start. But I have not yet gotten the request to work.

## Exploratory Data Analysis
* EDA can be found in the `notebooks\traffic_incidents.ipynb` Jupyter notebook.

## Model Feasibility
At the moment, this model does not seem like a viable solution. I attempted to choose various features and re-run the model, but was never able to break even 20% accuracy. It could be that there is simply not enough relevant information in the chosen features to make an accurate prediction of the Make of a vehicle. Given more time, I would attempt to run NLP on some of the text columns (Location, Violation Description) to see if there might be some correlation there.