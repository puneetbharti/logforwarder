import os
import json
import datetime

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def fetchLogFile():
    output_filename = os.path.normpath("travel.log")
    with open(output_filename, "r") as in_file:
        for line in in_file:
            formatLog(line)

def formatLog(line):
    formattedLine = {}
    formattedLine["@timestamp"]=datetime.datetime.now().strftime('%B %Y-%m-%d %H:%M:%S')
    formattedLine["message"]= line
    formattedLine["@version"] ='v1'
    postLogOutput(formattedLine)


def postLogOutput(postData):

    return 0

def verifyPattern():
    return False

def main():
    fetchLogFile()

if __name__ == '__main__':
    fetchLogFile()
