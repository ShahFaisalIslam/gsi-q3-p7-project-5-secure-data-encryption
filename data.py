# Data module
# Provides functions to store and retrieve data from file

import json
from base64 import standard_b64encode,standard_b64decode
DATA_FILE : str = "data.json"
ENCODED_DATA_KEYS = ["data","key","passkey"]

def store_data(data : dict) -> None:
    '''
    Stores given data in data file
    data: Dictionary representing data
    '''
    stored_data : dict = {}

    # Store the bytes as base64-encoded strings
    for key in data.keys():
        stored_data[key] = str(standard_b64encode(data[key]),encoding="ascii")

    # Open file
    with open(DATA_FILE,"w") as data_file:
        # Dump data into the file
        json.dump(obj=stored_data,fp=data_file,ensure_ascii=False)

def retrieve_data() -> dict:
    '''
    Retrieves data from the data file
    '''
    # Initialize data as dictionary with empty keys
    # in case the file fails to open
    data : dict = {
        "data" : "",
        "passkey": ""
        }

    try:
        with open(DATA_FILE) as data_file:
            data = json.load(data_file)
            for key in data.keys():
                data[key] = standard_b64decode(data[key])
    # Initialize file with data if it does not exist
    except FileNotFoundError:
        with open(DATA_FILE,"w") as data_file:
            json.dump(data,data_file,ensure_ascii=False)

    return data