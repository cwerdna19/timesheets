from docopt import docopt

usage = '''

Timesheet CLI.
Add time to and create spreadsheets.

Usage: timesheets.py [-h] [-n] [-iolu TIME] [-d DATE] [-f FILE]
    TIME    hh:tt:(ss)
    FILE    required for -niolu. specifies the new or existing excel sheet.

    -h      show this help
    -n      create a new timesheet
    -i      record time in
    -o      record time out
    -l      record lunch in
    -u      record lunch out
    -d      DATE [ddmmyy, "today", "tomorrow", "yesterday"]
    -s      NOTES

'''

time = clock

i = input("")
