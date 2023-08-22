# Canvas ICS to Apple Reminders

I regularly use Apple Reminders to keep track of my school assignments, sadly it does not support importing anything, so I have to manually import all my assignments.

**In progress project** to take any Canvas ICS file and import it into Apple Reminders

Likely will need to use EventKit and Swift. I don't know Swift yet so it may take a while.

## Usage

`pip install requests json`

`python main.py [url] [OPTIONAL: outpath]`

To get your canvas ICS file url, go to Calendar in Canvas, and click Calendar Feed on the right hand side.
Whatever outpath you choose is relative to the directory you run main.py from.

## Current progress made

* Built ICS parser which takes in Canvas ICS url and outputs as JSON format with assignment name, class, and due date

## Todo

* Implement EventKit for use with Apple Reminders
* Likely will rebuilt ICS parser in Swift
* Make this for general ICS, not just for Canvas assignment
