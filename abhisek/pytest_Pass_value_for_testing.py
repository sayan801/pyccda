import json
import Reg_exp_Emp_fields


class Testclass:
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""


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
        for elements in json_data:                           # Each elements is a tag under json_data
            # print "Details of ", elements                  # description of elements
            # print json_data[elements]                      # Each elements is a list of dictionaries
            for entry in range(len(json_data[elements])):    # entry stands for a dictionary from a list of dictionaries for elements
                email_id = json_data[elements][entry]['emailAddress']
                fname = json_data[elements][entry]['firstName']
                uid = json_data[elements][entry]['userId']
                reg = json_data[elements][entry]['region']
                flname = json_data[elements][entry]['preferredFullName']
                job_roll = json_data[elements][entry]['jobTitleName']
                lname = json_data[elements][entry]['lastName']
                contact = json_data[elements][entry]['phoneNumber']
                ecode = json_data[elements][entry]['employeeCode']

                # Here elements stands for Employees of an organisation and each entry stands for details of an Employee

                for item in json_data[elements][entry]:
                    if item == 'userId':
                        uid_value = Reg_exp_Emp_fields.check_userID(uid)
                        assert uid_value == True

                    if item == 'jobTitleName':
                        job_roll_value = Reg_exp_Emp_fields.check_jobTitleName(job_roll)
                        assert job_roll_value == True

                    if item == 'firstName':
                        fname_value = Reg_exp_Emp_fields.check_firstName(fname)
                        assert fname_value == True

                    if item == 'lastName':
                        lname_value = Reg_exp_Emp_fields.check_lastName(lname)
                        assert lname_value == True

                    if item == 'preferredFullName':
                        flname_value = Reg_exp_Emp_fields.check_preferredFullName(flname)
                        assert flname_value == True

                    if item == 'employeeCode':
                        ecode_value = Reg_exp_Emp_fields.check_employeeCode(ecode)
                        assert ecode_value == True

                    if item == 'region':
                        reg_value = Reg_exp_Emp_fields.check_region(reg)
                        assert reg_value == True

                    if item == 'phoneNumber':
                        contact_value = Reg_exp_Emp_fields.check_phoneNumber(contact)
                        assert contact_value == True

                    if item == 'emailAddress':
                        email_id_value = Reg_exp_Emp_fields.check_emailAddress(email_id)
                        assert email_id_value == True





