
import re


class Regular_exp:

    def __init__(self, element):
        self.element = element

    def check_userID(self):
        ''' Rule : UserID consists of [A-Z|a-z|0-9] '''
        ID = self.element
        match = re.search(r'\w+', ID)
        print match.group(0),
        if match:
            return True
        else:
            return False


    def check_jobTitleName(self):
        ''' Rule: Employee Job title starts with [A-Z] then multiple occurrence of [a-z] and 1 space, [A-Z] and multiple occurrences of [a-z] as optional. '''
        Job_Title = self.element
        match = re.search(r'(^[A-Z][a-z]+)( [A-Z][a-z]+)?$', Job_Title)
        if match:
            print "Job Title", match.group(0),
	    print "First part of Job title:", match.group(1),
            print "Second part of Job title:", match.group(2),

            return True
        else:
            return False


    def check_firstName(self):
        ''' Rule: Starts with [A-Z] the multiple occurrences of [a-z]. '''
        First_Name = self.element
        match = re.search(r'^[A-z][a-z]+$', First_Name)
        if match:
            print match.group(0),
            return True
        else:
            return False

    def check_lastName(self):
        ''' Rule: Starts with [A-Z] the multiple occurrences of [a-z]. '''
        Last_Name = self.element
        match = re.search(r'^[A-z][a-z]+$', Last_Name)
        if match:
            print match.group(0),
            return True
        else:
            return False


    def check_preferredFullName(self):
        ''' Rule: Combination of first and last names. '''
        Full_Name = self.element
        match = re.search(r'(^[A-Z][a-z]+) ([A-Z][a-z]+)$', Full_Name)
        if match:
            print "Full Name:", match.group(0),
            print "First Name:", match.group(1),
            print "Last Name:", match.group(2),
            return True
        else:
            return False


    def check_employeeCode(self):
        ''' Rule: Starts with 'E' and followed by multiple occurrences of [0-9].  '''
        Emp_Code = self.element
        match = re.search(r'^E\d+', Emp_Code)
        if match:
            print match.group(0),
            return True
        else:
            return False


    def check_region(self):
        ''' Rule: Short form of states in US.  '''
        Working_Place = self.element
        match = re.search(r'[A-Z]{2}', Working_Place)
        if match:
            print match.group(0),
            return True
        else:
            return False


    def check_phoneNumber(self):
        ''' Rule: Total 10 digits. First 3 digits for province code then followed by - and 7 digits.  '''
        Contact_Number = self.element
        match = re.search(r'\d{3}-\d{7}', Contact_Number)
        if match:
            print match.group(0),
            return True
        else:
            return False


    def check_emailAddress(self):
        ''' Rule: <host name>@<provider name>.<DNS type>  '''
        Email_Address = self.element
        match = re.search(r'(^\w+\.?\w+)@(\w+\.\w+)$', Email_Address)
        if match:
            print "Email Address:", match.group(0),
            print "Host part:", match.group(1),
            print "Domain part:", match.group(2),
            return True
        else:
            return False
