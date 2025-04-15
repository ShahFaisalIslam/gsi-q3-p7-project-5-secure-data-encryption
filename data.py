# Data module
# Provides functions to store and retrieve data from file

import json
DATA_FILE : str = "data.json"
ENCODED_DATA_KEYS = ["data","key","passkey"]

def store_data(data : dict) -> None:
    '''
    Stores given data in data file
    data: Dictionary representing data
    '''
    stored_data : dict = {}

    # Convert bytes in data into string
    for key in data.keys():
        if key in ENCODED_DATA_KEYS:
            stored_data[key] = str(data[key],encoding="latin-1")

    # Open file
    with open(DATA_FILE,"w") as data_file:
        # Dump data into the file
        json.dump(obj=stored_data,fp=data_file)

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
    # Initialize file with data if it does not exist
    except FileNotFoundError:
        with open(DATA_FILE,"w") as data_file:
            json.dump(data,data_file)
    # Convert encoded data back into string
    for key in data.keys():
        if key in ENCODED_DATA_KEYS:
            data[key] = bytes(data[key],encoding="latin-1")

    return data