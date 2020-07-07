import validators

def validate_subjectName(val,subjectName):
    if not subjectName:
        print("No subjectName provided")
        val = 1
        return val

    if len(subjectName) < 5 or len(subjectName) > 20:
        print("subjectName must be between 5 and 20 characters")
        val = 1
        return val

def validate_shortForm(val,shortForm):
    if not shortForm:
        print("No shortForm provided")
        val = 1
        return val

    if len(shortForm) < 2 or len(shortForm) > 5:
        print("shortForm must be between 2 and 5 characters")
        val = 1
        return val

def validate_staff(val,staff):
    if not staff:
        print("No staff provided")
        val = 1
        return val
    if len(staff) < 5 or len(staff) > 20:
        print("staff must be between 5 and 20 characters")
        val = 1
        return val
    return

def validate_year(val,year):
    if not year:
        print("No year provided")
        val = 1
        return val
    if (year<'1000') or (year > '2020') :
        print("year must be between 1000 and 2020 characters")
        val = 1
        return val

def check(question_data,val):
    subjectName = question_data['subjectName']
    shortForm = question_data['shortForm']
    staff = question_data['staff']
    year = question_data['year']
    url = question_data['url']

    #checking for valid subjectName
    value = validate_subjectName(val,subjectName)
    if (value == 1):
        return value
    #checking for valid shortForm
    value = validate_shortForm(val, shortForm)
    if (value == 1):
        return value
    # checking for valid staff
    value = validate_staff(val, staff)
    if (value == 1):
        return value

    #checking for valid year
    value = validate_year(val, year)
    if (value == 1):
        return value

    #checking for valid url
    valid = validators.url(url)
    if valid == True:
        print("Url is valid")
    else:
        value = 1
        print("Invalid url")
        return value

    return value