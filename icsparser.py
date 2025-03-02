from datetime import datetime

class ICSParser():
    '''
    Takes in ics file and outputs it into dictionary format
    
    {
        AssignmentName : 
        {
            Date: MMDDYYYY,
            Class : class,
        }
        ...
    }

    '''
    def parse(self, text):
        text = text.split("BEGIN:VEVENT")
        event = {}
        for item in text:
            print(item)
            if 'SUMMARY:' in item:
                assignmentName = item.split("SUMMARY:")[1].split('URL;')[0]
                className, assignmentName = self.getSplitString(assignmentName, "[", " (")
                date = None
                if 'DTSTART;' in item: # purely a date with default due date at 11:59pm, #DTSTART;VALUE=DATE;VALUE=DATE:20250322
                    date = self.cleanString(str(item.split("VALUE=DATE:")[1].split("CLASS:")[0]), "\r", "\n")
                elif 'DTSTART:' in item: # includes date and time, #DTSTART:20250317T183000Z\nDTEND:20250317T183000Z
                    date = self.cleanString(str(item.split("DTSTART:")[1].split("DTEND:")[0]), "\r", "\n")

                event[assignmentName] = {
                    "Date" : date,
                    "Class" : className
                }
        return event

    def cleanString(self, string: str, *args):
        for str in args:
            splitstring = string.split(str)
            splitstring = [x.lstrip().rstrip() for x in splitstring]
            string = ''.join(splitstring)
        return string

    def getSplitString(self, string: str, str1: str, str2: str):
        idx1 = string.rfind(str1)
        idx2 = string.rfind(str2)

        splitStr1 = self.cleanString(string[idx1 + len(str1): idx2], "\r", "\n")
        splitStr2 = self.cleanString(string[0:idx1-1], "\r", "\n", "\\")

        return splitStr1, splitStr2