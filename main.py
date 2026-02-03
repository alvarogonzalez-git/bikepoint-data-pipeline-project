# Import libraries
from datetime import datetime
from dotenv import load_dotenv
import os
import logging

# Import modules
from modules import extract, load

# Define runtime timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

# Create log directories if they do not exist
os.makedirs('logs/extract', exist_ok=True)
os.makedirs('logs/load', exist_ok=True)

# EXTRACT logging config
# Searching for and assign logger defined in extract.py module
extract_logger = logging.getLogger('modules.extract')
extract_logger.setLevel(logging.INFO)

# Create the file handler for extract.py with dynamic log filename
extract_handler = logging.FileHandler(f'logs/extract/{timestamp}_extract.log', encoding='utf-8')
extract_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
extract_logger.addHandler(extract_handler)

# Ensures extract handler doesn't propagate to parent directories
extract_logger.propagate = False 


# LOAD logging config
# Searching for and assign logger defined in load.py module
load_logger = logging.getLogger('modules.load')
load_logger.setLevel(logging.INFO)

# Create the file handler for load.py with dynamic log filename
load_handler = logging.FileHandler(f'logs/load/{timestamp}_load.log', encoding='utf-8')
load_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
load_logger.addHandler(load_handler)

# Ensures load handler doesn't propagate to parent directories
load_logger.propagate = False


# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = 'https://api.tfl.gov.uk//BikePoint'

# Load .env file
load_dotenv()

# Assign .env credentials to variables
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

# Extract data from BikePoint, save to "data" folder and log
extract.extract_function(url, 3, timestamp)

# Read files from "data" folder, upload to S3 bucket and log
load.load_function('extracted_data', AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME)