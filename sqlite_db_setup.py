from utils import get_clean
import logging
import sqlite3
from pathlib import Path

# Create logger object
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s")

corrupted_data = 'https://s3-us-west-2.amazonaws.com/pcadsassessment/parking_citations.corrupted.csv'

# Grab data from s3 and clean
df = get_clean(source_file = corrupted_data)

# Load dataframe into sqlite db
Path('citations.db').touch()
conn = sqlite3.connect('citations.db')
logging.info('Writing to table...')
df.to_sql('vehicles', conn)
logging.info('Complete')