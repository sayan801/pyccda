'''
Objectives :
1. Input a JSON file from user. (here, Employees.json)
2. Read the JSON file and print the data on console
3. Create methods (units) for each field of an employee and check the fields values using regular expression.
4. Perform unit testing for each unit using Python module unittest.
'''

import json
import Reg_exp_Emp_fields  # Module to check fields values using regular expression for each employee.
import unittest


class myUnitTesting(unittest.TestCase):

    def test_email_Id(self, email_id):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(email_id)
        self.assertTrue(reg_exp.check_emailAddress(), 'User Email Address is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_emailAddress()

    def test_first_Name(self, first_name):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(first_name)
        self.assertTrue(reg_exp.check_firstName(), 'User First name is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_firstName()

    def test_user_ID(self, u_id):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(u_id)
        self.assertTrue(reg_exp.check_userID(), 'User ID is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_userID()

    def test_region(self, region):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(region)
        self.assertTrue(reg_exp.check_region(), 'User working Region is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_region()

    def test_preferredFullName(self, full_name):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(full_name)
        self.assertTrue(reg_exp.check_preferredFullName(), 'User Full name is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_preferredFullName()

    def test_job_Title(self, job_title):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(job_title)
        self.assertTrue(reg_exp.check_jobTitleName(), 'User Job title is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_jobTitleName()

    def test_last_Name(self, last_name):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(last_name)
        self.assertTrue(reg_exp.check_lastName(), 'User Last name is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_lastName()

    def test_phone_Number(self, contact_num):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(contact_num)
        self.assertTrue(reg_exp.check_phoneNumber(), 'User Contact Number is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_phoneNumber()


    def test_employee_Code(self, emp_code):
        reg_exp = Reg_exp_Emp_fields.Regular_exp(emp_code)
        self.assertTrue(reg_exp.check_employeeCode(), 'User Employee code is OK')
        with self.assertRaises(TypeError):
            reg_exp.check_employeeCode()

    def test_sample_json_file(self):
        """Test all sample json files in the testdata directory."""
        json_file = "Employees.json"
        json_fp = open(json_file, 'r')
        json_content = json_fp.read()
        json_fp.seek(0)
        json_data = json.load(json_fp)
        json_fp.close()
        '''
            json.load(file_pointer) where file_pointer open json file in read mode. This method creates and returns a dictionary
            from JSON file
            json.loads(file_pointer(read)) where file_pointer.read() is a string and rest is same as json.load(). But, we need
            to use pprint() to print the dictionary
        '''
        for elements in json_data:                         # Each elements is a tag under json_data
            print "Details of ", elements                  # description of elements
            print json_data[elements]                      # Each elements is a list of dictionaries
            for entry in range(len(json_data[elements])):  # entry stands for a dictionary from a list of dictionaries for elements
                print json_data[elements][entry]

                # Here elements stands for Employees of an organisation and each entry stands for details of an Employee'''
                print "Details of Employee[%d]" % entry
                for item in json_data[elements][entry]:
                    if item == 'userId':
                        self.test_user_ID(json_data[elements][entry]['userId'])
                    if item == 'jobTitleName':
                        self.test_job_Title(json_data[elements][entry]['jobTitleName'])
                    if item == 'firstName':
                        self.test_first_Name(json_data[elements][entry]['firstName'])
                    if item == 'lastName':
                        self.test_last_Name(json_data[elements][entry]['lastName'])
                    if item == 'preferredFullName':
                        self.test_preferredFullName(json_data[elements][entry]['preferredFullName'])
                    if item == 'employeeCode':
                        self.test_employee_Code(json_data[elements][entry]['employeeCode'])
                    if item == 'region':
                        self.test_region(json_data[elements][entry]['region'])
                    if item == 'phoneNumber':
                        self.test_phone_Number(json_data[elements][entry]['phoneNumber'])
                    if item == 'emailAddress':
                        self.test_email_Id(json_data[elements][entry]['emailAddress'])

                    print "\n\n"


# Main namespace
if __name__ == '__main__':
    unittest.main()







