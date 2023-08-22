import requests
from icsparser import ICSParser
import argparse
from tojson import toJson

def main():
    # url = "https://canvas.oregonstate.edu/feeds/calendars/user_Isd3z5yGcoNDhxfzoUWCXliURkw5V1sm7mT5SV5l.ics"

    # process args
    args = argsparser.parse_args()
    url = args.url
    outfile = args.path

    # get ICS info
    importedICS = str(requests.get(url).text)

    # parse ICS
    parser = ICSParser()
    parsedICS = parser.parse(importedICS)

    # send parsed ICS information to JSON
    toJson(parsedICS, outfile)

if __name__ == '__main__':
    argsparser = argparse.ArgumentParser()
    argsparser.add_argument("url", help="URL link to .ICS calendar")
    argsparser.add_argument("--path", "-p", help="Outfile path for JSON", default="./")

    main()
