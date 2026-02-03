import requests
import os
import json
import time
import logging

# Activate logger and assign name using .py filename
logger = logging.getLogger(__name__)

# Extract function
def extract_function(url, number_of_tries, timestamp):
    '''
    Designed for extracting data for TfL BikePoints
    
    :param url: API call URL
    :param number_of_tries: max number of times API retries connection
    :param logger: assigns logger to function
    :param timestamp: runtime timestamp
    '''

    count = 0

    # While loop that ensures retires does not exceed number_of_retries variable above
    while count < number_of_tries:

        # Make API call and status code variable created
        response = requests.get(url, timeout=10)
        response_code = response.status_code

        # Wrapping folder creation, filepath creation, file write logic into an if that checks response status code is successful "== 200". Response reason will be returned if not 
        if response_code == 200:
            # Assign json data to variable
            response_json = response.json()

            # Create variable for data folder creation logic
            data_dir = 'extracted_data'

            # Checking if data folder exists. If it doesn't exist, a folder is created
            if os.path.exists(data_dir):
                pass
            else:
                os.mkdir(data_dir)

            # Created filepath using filename variable and folder variable
            filepath = f'{data_dir}/{timestamp}.json'

            # try/except block to provide information if there are any issues writing the file
            try:
                # Writing data file
                with open(filepath, 'w') as file:
                    json.dump(response_json,file)
                # Print success message
                print(f'Download successful at {timestamp} 😊. Files saved to {data_dir}.')
                # Logger will note a message if file write is successful
                logger.info(f'Download successful at {timestamp} 😊. Files saved to {data_dir}.') 
            except Exception as e:
                print(f'An error occurred: {e}.')
                # Logger will note exception error if file write is unsuccessful
                logger.error(f'An error occurred: {e}.')             
            break

        elif response_code > 499 or response_code < 200:
            # Retry with 10 second wait
            print(f'Connection Error: {response.reason}. Retrying...')
            # Logger notes response reason when response code is 100s or 500s
            logger.warning(f'Connection Error: {response.reason}. Retrying...')     
            # The time.sleep function makes the script wait 10 seconds before retrying
            time.sleep(10)
            count += 1

        else:
            print(f'Error: {response.reason}. Check your credentials and try again.')
            # Logger notes response reason when response code is not 100s, 200s, 500s
            logger.error(f'Error: {response.reason}. Check your credentials and try again.')             
            break