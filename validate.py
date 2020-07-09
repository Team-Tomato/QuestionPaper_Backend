import validators
import re

def validate_sName(val,sName):
    if not sName:
        print(sName,"No Name provided")
        val = 1
        return val

    if len(sName) < 5 or len(sName) > 20:
        print(sName,"given Name must be between 5 and 20 characters")
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
    value = validate_sName(val,subjectName)
    if (value == 1):
        return value
    #checking for valid shortForm
    value = validate_shortForm(val, shortForm)
    if (value == 1):
        return value
    # checking for valid staff
    value = validate_sName(val, staff)
    if (value == 1):
        return value

    #checking for valid year
    value = validate_year(val, year)
    if (value == 1):
        return value

    #checking for valid url
    valid = validators.url(url)
    if valid == True:
        return value
    else:
        value = 1
        print("Invalid url")
        return value

    return value

#checking for book
def validate_Name(val,Name):
    if not Name:
        print(Name,"No Name provided")
        val = 1
        return val

    if len(Name) < 5 or len(Name) > 20:
        print(Name,"given Name must be between 5 and 20 characters")
        val = 1
        return val

def validate_isbn(val,isbn):
    if not isbn:
        print("No year provided")
        val = 1
        return val
    if (len(isbn)<10) or (len(isbn) > 13) :
        print("isbn must be between 10 and 13 characters")
        val = 1
        return val

def check_book(book_data,val):
    title = book_data['title']
    author = book_data['author']
    publisher = book_data['publisher']
    isbn = book_data['isbn']
    url = book_data['url']


    #checking for valid title
    value = validate_Name(val,title)
    if (value == 1):
        return value
    # checking for valid author
    value = validate_Name(val, author)
    if (value == 1):
        return value

    # checking for valid publisher
    value = validate_Name(val, publisher)
    if (value == 1):
        return value

    # checking for valid isbn
    value = validate_isbn(val, isbn)
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



# checking for contact us
def validate_email(val,email):
    if not email:
        print("No year provided")
        val = 1
        return val
    if not re.match("[^@]+@[^@]+\.[^@]+", email):
        print("Provided email is not an email address")
        val = 1
        return val

def checking_contactus(contact_data, val):
    name = contact_data['name']
    email = contact_data['email']
    # message = contact_data['message']

    #checking for name
    value = validate_Name(val, name)
    if (value == 1):
        return value

    #checking for email
    value = validate_email(val,email)
    if (value == 1):
        return value

    return value



