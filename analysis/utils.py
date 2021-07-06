import pandas as pd

def get_clean(source_file):
    """Generate a clean data frame from source file"""
    print('Reading from source...')
    df = pd.read_csv(source_file)
    print('Cleaning up source csv...')
    # Drop rows with too much NA data
    df.drop(['Meter Id', 'Marked Time', 'VIN'], axis=1, inplace=True)
    # Drop rows missing "Make"
    print('Import complete')
    return df[df['Make'].notna()]

def get_top_25(df):
    """Generate list of top 25 makes"""
    print('Generating top 25 Makes...')
    common_makes = df.groupby('Make')['Ticket number'].count().sort_values(ascending=False).head(25)
    return [make for make in common_makes.index]
