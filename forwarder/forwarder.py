import os
import json
import datetime
import requests

config = {
    "host":"http://localhost:3000/save/",
    "paths":["travel.log"],
    "pattern":"",
    "app_name":"travel"
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
    formattedLine["@timestamp"]=datetime.datetime.now().strftime('%B %Y-%m-%d %H:%M:%S')
    formattedLine["message"]= line
    formattedLine["@version"] ='v1'
    formattedLine["app"] = config["app_name"]
    postLogOutput(formattedLine)


def postLogOutput(postData):
    response = requests.post(config['host'], json=postData)
    print(response)

def verifyPattern():
    return False

def main():
    fetchLogFile()

if __name__ == '__main__':
    fetchLogFile()
