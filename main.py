# gather information from the user
dept = input('Enter the department code: ')
course = input('Enter the course number: ')
section = input('Enter the section number: ')

error = False

# Section Number Tables
section_nums = {
    '01': {
        'times': '8:00 - 8:50 am',
        'days': 'Daily'
    },
    '02': {
        'times': '9:00 - 9:50 am',
        'days': 'Daily'
    },
    '03': {
        'times': '10:00 - 10:50 am',
        'days': 'Daily'
    },
    '04': {
        'times': '11:00 - 11:50 am',
        'days': 'Daily'
    },
    '05': {
        'times': '12:00 - 1:05 pm',
        'days': 'MTWTh'
    },
    '06': {
        'times': '1:15 - 2:20 pm',
        'days': 'MTWTh'
    },
    '08': {
        'times': '6:00 - 8:20 pm',
        'days': 'MW'
    },
    '09': {
        'times': '6:00 - 8:20 pm',
        'days': 'TTh'
    }
}

def lookup(code):
    try:
        return section_nums[code]
    except KeyError:
        return 'unknown'

def output(meeting):
    global error
    try:
        return 'Your course {} {}-{} meets {}, {}'.format(
            dept,
            course,
            section,
            meeting.get('times'),
            meeting.get('days'))
    except AttributeError:
        error = True;
        return 'ERROR: Unrecognized section number.'

# determine when the class meets: the error state is triggered here
meeting = lookup(section)
printout = output(meeting)


if not error:
    if not dept.isupper():
        print('WARNING: departement code is not upper-case.')
        dept = dept.upper()

    if len(course) != 3:
        print('WARNING: course number is not 3-digits.')

    try:
        val = int(course)
    except ValueError:
        print('WARNING: course number is not numeric.')

# output the information to the user
print(printout)
