## Ifeanyi Ibe
## Lab 3: Section Times
##


section01 = "8:00 - 8:50am, Daily"
section02 = "9:00 - 9:50am, Daily"
section03 = "10:00 - 10:50am, Daily"
section04 = "11:00 - 11:50am, Daily"
section05 = "12:00 - 1:05pm, MTWTh"
section06 = "1:15 - 2:20pm, MTWTh"
section08 = "6:00 - 8:20pm, MW"
section09 = "6:00 - 8:20pm, TTh"


# gather information from the user
dept = input('Enter the department code: ')
course = input('Enter the course number: ')
section = input('Enter the section number: ')

# Initialize some values
error = False
output = ""

def prepare(selection):
    return 'Your course {} {}-{} meets {}'.format(
        dept,
        course,
        section,
        selection)

if section == str("01"):
    output = prepare(section01)
elif section == str("02"):
    output = prepare(section02)
elif section == str("03"):
    output = prepare(section03)
elif section == str("04"):
    output = prepare(section04)
elif section == str("05"):
    output = prepare(section05)
elif section == str("06"):
    output = prepare(section06)
elif section == str("08"):
    output = prepare(section08)
elif section == str("09"):
    output = prepare(section09)
else :
    error = True
    output = "ERROR: Unrecognized section number."

# do error checks only if the section number is valid
if not error:
    if not dept.isupper():
        print('WARNING: departement code is not upper-case.')
        dept = dept.upper()

    if len(course) != 3:
        print('WARNING: course number is not 3-digits.')

    if not course.isnumeric():
        print('WARNING: course number is not numeric.')

# output the information to the user
print(output)
