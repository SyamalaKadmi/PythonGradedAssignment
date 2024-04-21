# Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
# ●       The program should read a configuration file (you can provide them with a sample configuration file).
# ●       It should extract specific key-value pairs from the configuration file.
# ●       The program should store the extracted information in a data structure (e.g., dictionary or list).
# ●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
# ●       Finally save the output file data as JSON data in the database.
# ●       Create a GET request to fetch this information.


### Please run below steps to validate Get operation. 
### In the terminal, run 
#1. py -3 -m venv .venv
#2. .venv\Scripts\activate
#3. pip install Flask
#4. flask --app config_mgmt run


import configparser
import os.path
import json
from django.contrib.postgres.fields import JSONField
from django.db import models
import requests

class cnfg_mgmt(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name

from flask import Flask

path = 'C:\python\GradedAssignment\config_mgmt.ini'
config = configparser.ConfigParser()
checkFilePath = os.path.isfile(path)

app = Flask(__name__)
@app.route("/")
def conf_mgmt():
    if not checkFilePath: #checking file path
        print("Invalid file path: ", path)
    elif not os.access(path, os.R_OK): # checking if the file is readable
        print("The file cannot be read", path)
    else:
        config.read(path)#reading configuration file
        config_dict = dict()
        sections=config.sections()
        for section in sections:
            items=config.items(section)
            config_dict[section]=dict(items) #storing extracting information in dictionary data structure
            config_json = json.dumps(config_dict) # save the output file data as JSON data 
            cnfg_mgmt.objects.create(name='ConfigManagement', data=config_json) # Storing JSON data to database
    return config_json


URL = "http://127.0.0.1:5000"


 
# defining a params dict for the parameters to be sent to the API
PARAMS = {conf_mgmt()}
 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()
 
print("Configuration File Parser Results:")
print(conf_mgmt())






