import pandas as pd
import pickle
from sklearn import metrics
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

print('Getting data set...')
# dataset = pd.read_csv('https://s3-us-west-2.amazonaws.com/pcadsassessment/parking_citations.corrupted.csv')
dataset = pd.read_csv('parking_citations.corrupted.csv')

def prepare_data(df):
    # Drop rows missing our output variable
    data = dataset[dataset['Make'].notna()]
    # Let's cut down the rows so we can make this usable in our slow environment
    data = data.sample(50000, random_state=42)
    # Drop rows with too much NA data
    data.drop(['Meter Id', 'Marked Time', 'VIN'], axis=1, inplace=True)
    # Let's remove all remaining NA values
    return data.dropna()

# def make_dummies(df, features):
#     enc = OneHotEncoder(handle_unknown='ignore')
#     return pd.DataFrame(enc.fit_transform(df[features]).toarray())
#     # return df.join(enc_df)

def get_top_25(df):
    """Generate list of top 25 makes"""
    common_makes = df.groupby('Make')['Ticket number'].count().sort_values(ascending=False).head(25)
    return [make for make in common_makes.index]

def build_model(df, output_var, features):
    print('Building model...')
    # Set output var
    y = df[output_var]
    # Set our features
    # X = make_dummies(df, features)
    # X = pd.get_dummies(df[features])
    X = df[features]
    # Split our dataset into training/test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state = 42)
    # Set up our Random Forest
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    return model, y_pred

df = prepare_data(dataset)
# features = ['RP State Plate', 'Body Style', 'Color', 'Agency', 'Fine amount']
features = ['Issue time', 'Plate Expiry Date', 'Agency', 'Fine amount', 'Latitude', 'Longitude']
top_25 = get_top_25(df)
# Write top 25 to file for later
pickle.dump(top_25, open('top_25.pkl', 'wb'))

model, pred = build_model(df, 'Make', features)

# Saving model to disk
print('Saving model to disk...')
pickle.dump(model, open('make_model.pkl', 'wb'))

# Loading model to compare the results
test_model = pickle.load(open('make_model.pkl', 'rb'))

test_set = {
    'Issue time': 1710.0,
    'Plate Expiry Date': 201605.0,
    'Agency': 54.0,
    'Fine amount': 73,
    'Latitude': 99999.0,
    'Longitude': 99999.0
}

test_df = pd.DataFrame(test_set, index = [0])
print(test_df)
# prepared_test = pd.get_dummies(test_df)
# prepared_test = prepared_test.reindex(labels=pd.get_dummies(df[features]).columns, axis=1)
print('Prediction:', model.predict(test_df))