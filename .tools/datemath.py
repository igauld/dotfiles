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
    
def print_help():
    print(help)
    exit()

def valid_operator(operator):
    return operator in ["+", "-"]
    
# hack...
def fix_year(year):
    if len(year) == 4:
        return year

    return "20" + year

def fix_day(day):
    if len(day) < 2:
        return "0" + day

    return day

# iso format is yyyy-mm-dd but we want to be able to send in
# dd-mm-yyyy or dd-mm-yy or yyyy-mm-dd
# note that yy-mm-dd is NOT supported
def parse_date(s):
    # seperators are - , / and \
    values = re.split("-|,|/|\\.|\\\\", s)
    if len(values) != 3:
        print_help()

    month = values[1]
    if len(values[0]) > 2:
        year = values[0]
        day = values[2]
    else:
        year = values[2]
        day = values[0]
    
    return fix_day(day), month, fix_year(year)

def date_sub_scalar(d, value):
    return d - datetime.timedelta(days=value)

def date_diff(d1, d2):
    return d1 - d2

def date_add(day, month, year, value):
    d = datetime.date.fromisoformat(f"{year}-{month}-{day}")
    return d + datetime.timedelta(days=value)


if len(sys.argv) != 4:
    print_help()
    
arg1 = sys.argv[1]
operator = sys.argv[2]
arg2 = sys.argv[3]

if not arg1 or not operator or not arg2:
    print_help()
    
if not valid_operator(operator):
    print_help()

result = 0

if operator == "+":
    if not arg2.isnumeric():
        print_help()

    day, month, year = parse_date(arg1)

    result = date_add(day, month, year, int(arg2))

elif operator == "-":
    day, month, year = parse_date(arg1)
    d1 = datetime.date.fromisoformat(f"{year}-{month}-{day}")

    if not arg2.isnumeric():
        day, month, year = parse_date(arg2)
        d2 = datetime.date.fromisoformat(f"{year}-{month}-{day}")

        result = date_diff(d1, d2)
    else:
        result = date_sub_scalar(d1, int(arg2))
else:
    print_help()
    
print(f"Result: {result}")
