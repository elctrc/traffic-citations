import logging
import pandas as pd

# Create logger object
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s")

def get_clean(source_file):
    # Grab data source from s3
    logging.info('Reading from source...')
    df = pd.read_csv(source_file)
    logging.info('Cleaning up source csv...')
    # Drop rows with too much NA data
    df.drop(['Meter Id', 'Marked Time', 'VIN'], axis=1, inplace=True)
    # Drop rows missing "Make"
    logging.info('Import complete')
    return(df[df['Make'].notna()])