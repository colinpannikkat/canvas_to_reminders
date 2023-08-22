import json
from datetime import datetime

date = datetime.now()

def toJson(dict: dict, output: str):
    '''
        Takes Python dictionary and converts it into JSON file
    '''

    try:
        OUTFILE = open(f'{output}calendar.json', "+x")
    except Exception as e:
        i = 1
        goodPath = False
        while not goodPath:
            OUTFILE, goodPath = openFile(f'{output}calendar{i}.json')
            i+=1

    json.dump(dict, OUTFILE, indent=4)

def openFile(file):
    try:
        OUTFILE = open(file, "+x")
    except:
        return '', False
    return OUTFILE, True
    
