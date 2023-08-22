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
            if 'SUMMARY:' in item:
                assignmentName = item.split("SUMMARY:")[1].split('URL:')[0]
                className, assignmentName = self.getSplitString(assignmentName, "[", " (")
                date = self.cleanString(str(item.split("VALUE=DATE:")[1].split("CLASS:")[0]), "\r", "\n")
                event[assignmentName] = {
                    "Date" : date,
                    "Class" : className
                }
        return event

    def cleanString(self, string, *args):
        for str in args:
            splitstring = string.split(str)
            splitstring = [x.lstrip() for x in splitstring]
            string = ''.join(splitstring)
        return string

    def getSplitString(self, string, str1, str2):
        idx1 = string.find(str1)
        idx2 = string.find(str2)

        splitStr1 = self.cleanString(string[idx1 + len(str1): idx2], "\r", "\n")
        splitStr2 = self.cleanString(string[0:idx1-1], " [", "(")

        return splitStr1, splitStr2

        
            
