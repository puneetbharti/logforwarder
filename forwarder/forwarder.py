"""
@config
 host: api host
 path: path of the file
 type: grok, json or keep it empty
 pattern: if it is a grok and specify the pattern

Pattern matching is done by using grok library
it can be of two types either json or grok

"""
import os
import json
import datetime
import requests
from pygrok import Grok


config = {
    "host":"http://localhost:3000/save/",
    "paths":["travel.log", "grok.log"],
    "type": "grok",
    "pattern": "%{WORD:name} is %{WORD:gender}, %{NUMBER:age:int} years old and weighs %{NUMBER:weight:float} kilograms",
    "app_name": "travel"
}


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def fetchLogFile():
    for file in config["paths"]:
        output_filename = os.path.normpath(file)
        with open(output_filename, "r") as in_file:
            for line in in_file:
                formatLog(line)

def formatLog(line):
    formattedLine = {}

    if(config['type'] == 'json'):
        if(is_json(line)):
            formattedLine.update(json.loads(line))
        else:
            formattedLine['message'] = line

    elif(config['type'] == 'grok'):
        grok = Grok(config["pattern"])
        if (type(grok.match(line)).__name__ == 'NoneType'):
            formattedLine["message"] = line
        else:
            formattedLine = grok.match(line)
    else:
        formattedLine["message"] = line


    formattedLine["@timestamp"]=datetime.datetime.now().strftime('%B %Y-%m-%d %H:%M:%S')
    formattedLine["@version"] ='v1'
    formattedLine["app"] = config["app_name"]

    postLogOutput(json.dumps(formattedLine))


def postLogOutput(postData):
    response = requests.post(config['host'], json=json.loads(postData))
    if(response.status_code != 200):
        raise Exception("Unable to send the data")
    else:
        return True



fetchLogFile()
