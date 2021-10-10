help = """Simple date arithmetic.  Three operations, plus or minus a scalar or 
minus another date.  

datemath.py 23-05-21 + 14
datemath.py 23-05-21 - 14
datemath.py 23-05-21 - 15-04-21

Dates can be of the following forms:

23-1-21
23/01/2021
2021-01-23

The following form:

21-1-23 is not allowed, short dates must have the year in the right hand
position.

"""

import sys
import datetime
import re
    
def printHelp():
    print(help)
    exit()

def validOperator(operator):
    return operator in ["+", "-"]
    
# hack...
def fixYear(year):
    if len(year) == 4:
        return year

    return "20" + year


# iso format is yyyy-mm-dd but we want to be able to send in
# dd-mm-yyyy or dd-mm-yy or yyyy-mm-dd
# note that yy-mm-dd is NOT supported
def parseDate(s):
    # seperators are - , / and \
    values = re.split("-|,|/|\\.|\\\\", s)
    if len(values) != 3:
        printHelp()

    month = values[1]
    if len(values[0]) > 2:
        year = values[0]
        day = values[2]
    else:
        year = values[2]
        day = values[0]
    
    return day, month, fixYear(year)

def dateSubScalar(d, value):
    return d - datetime.timedelta(days=value)

def dateDiff(d1, d2):
    return d1 - d2

def dateAdd(day, month, year, value):
    d = datetime.date.fromisoformat(f"{year}-{month}-{day}")
    return d + datetime.timedelta(days=value)


if len(sys.argv) != 4:
    printHelp()
    
arg1 = sys.argv[1]
operator = sys.argv[2]
arg2 = sys.argv[3]

if not arg1 or not operator or not arg2:
    printHelp()
    
if not validOperator(operator):
    printHelp()

result = 0

if operator == "+":
    if not arg2.isnumeric():
        printHelp()

    day, month, year = parseDate(arg1)

    result = dateAdd(day, month, year, int(arg2))

elif operator == "-":
    day, month, year = parseDate(arg1)
    d1 = datetime.date.fromisoformat(f"{year}-{month}-{day}")

    if not arg2.isnumeric():
        day, month, year = parseDate(arg2)
        d2 = datetime.date.fromisoformat(f"{year}-{month}-{day}")

        result = dateDiff(d1, d2)
    else:
        result = dateSubScalar(d1, int(arg2))
else:
    printHelp()
    
print(f"Result: {result}")
