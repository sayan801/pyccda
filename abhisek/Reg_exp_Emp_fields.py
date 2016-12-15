
import re

def check_userID(ID):
    ''' Rule : UserID consists of [A-Z|a-z|0-9] '''
    match = re.search(r'\w+', ID)
    #print match.group(0),
    if match:
        return True
    else:
        return False


def check_jobTitleName(Job_Title):
    ''' Rule: Employee Job title starts with [A-Z] then multiple occurrence of [a-z] and 1 space, [A-Z] and multiple
    occurrences of [a-z] as optional. '''
    match = re.search(r'(^[A-Z][a-z]+)( [A-Z][a-z]+)?$', Job_Title)
    if match:
        '''print "Job Title", match.group(0),
        print "First part of Job title:", match.group(1),
        print "Second part of Job title:", match.group(2), '''
        return True
    else:
        return False


def check_firstName(First_Name):
    ''' Rule: Starts with [A-Z] the multiple occurrences of [a-z]. '''
    match = re.search(r'^[A-z][a-z]+$', First_Name)
    if match:
        #print match.group(0),
        return True
    else:
        return False

def check_lastName(Last_Name):
    ''' Rule: Starts with [A-Z] the multiple occurrences of [a-z]. '''
    match = re.search(r'^[A-z][a-z]+$', Last_Name)
    if match:
        #print match.group(0),
        return True
    else:
        return False


def check_preferredFullName(Full_Name):
    ''' Rule: Combination of first and last names. '''
    match = re.search(r'(^[A-Z][a-z]+) ([A-Z][a-z]+)$', Full_Name)
    if match:
        '''print "Full Name:", match.group(0),
        print "First Name:", match.group(1),
        print "Last Name:", match.group(2), '''
        return True
    else:
        return False


def check_employeeCode(Emp_Code):
    ''' Rule: Starts with 'E' and followed by multiple occurrences of [0-9].  '''
    match = re.search(r'^E\d+', Emp_Code)
    if match:
        #print match.group(0),
        return True
    else:
        return False


def check_region(Working_Place):
    ''' Rule: Short form of states in US.  '''
    match = re.search(r'[A-Z]{2}', Working_Place)
    if match:
        #print match.group(0),
        return True
    else:
        return False


def check_phoneNumber(Contact_Number):
    ''' Rule: Total 10 digits. First 3 digits for province code then followed by - and 7 digits.  '''
    match = re.search(r'\d{3}-\d{7}', Contact_Number)
    if match:
        #print match.group(0),
        return True
    else:
        return False


def check_emailAddress(Email_Address):
    ''' Rule: <host name>@<provider name>.<DNS type>  '''
    match = re.search(r'(^\w+\.?\w+)@(\w+\.\w+$)', Email_Address)
    if match:
        '''print "Email Address:", match.group(0),
        print "Host part:", match.group(1),
        print "Domain part:", match.group(2), '''
        return True
    else:
        return False
