"""Unit tests for ccda.py."""

import ccda
import os
import unittest
import json
import logging

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), '../testdata')
logging.basicConfig(filename='Vitals_test.log', filemode='w', format='%(asctime)s--%(levelname)s:--%(message)s',
                        level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %P')
'''vital_code = None
vital_dict = {"Height": None, "Height_lying": None, "BMI": None, "BP_Diastolic": None, "BP_Systolic": None,
              "Weight": None, "Temperature": None, "Heart_Rate": None, "Respiratory_Rate": None,
              "Oxygen_Saturation": None} '''

fp_medication = None
fp_immunization = None
fp_problem = None
fp_lab_code = None
fp_lab_result = None
fp_procedure = None

#class CcdaDocumentTestCase(unittest.TestCase):
  #def _test_to_csv(self, fp):
  #  """Verify CCDA document can be converted to a CSV file."""
  #  ccda_doc = ccda.CcdaDocument(fp)
  #  ccda_csv = ccda_doc.to_csv()
  #  self.assertTrue(ccda_csv)
  # TODO: Implement stronger test. Verify generated CSV against testdata.


def unicode_OR_String(variable):  # variable : "kg/m\u00b2" or "kg/m"
    if isinstance(variable, unicode):
        return variable.encode('utf-8')
    elif isinstance(variable, str):
        return variable


def call_medication(medi_dict):
    '''
    medi_dict: {"code": "445655", "name": "azithromycin Oral Tablet 500 mg", "code_system": ""}
    '''

    if fp_medication is None:
        global fp_medication
        fp_medication = open("medication.txt", 'a+b')
        code = unicode_OR_String(medi_dict["code"])
        name = unicode_OR_String(medi_dict["name"])
        code_system = unicode_OR_String(medi_dict["code_system"])
        #fp_medication.write(code + " " + name + " " + code_system + "\n")
        fp_medication.write(code_system + "\n")
    else:
        fp_medication.seek(0)
        file_content = fp_medication.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(medi_dict["code"])
        name = unicode_OR_String(medi_dict["name"])
        code_system = unicode_OR_String(medi_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_medication.write(code + " " + name + " " + code_system + "\n")
                fp_medication.write(code_system + "\n")
        del code_list


def call_immunization(immun_dict):
    '''
    immun_dict: {"code": "88", "name": "influenza, NOS", "code_system": "2.16.840.1.113883.12.292"}
    '''
    if fp_immunization is None:
        global fp_immunization
        fp_immunization = open("immunization.txt", 'a+b')
        code = unicode_OR_String(immun_dict["code"])
        name = unicode_OR_String(immun_dict["name"])
        code_system = unicode_OR_String(immun_dict["code_system"])
        #fp_immunization.write(code + " " + name + " " + code_system + "\n")
        fp_immunization.write(code_system + "\n")
    else:
        fp_immunization.seek(0)
        file_content = fp_immunization.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(immun_dict["code"])
        name = unicode_OR_String(immun_dict["name"])
        code_system = unicode_OR_String(immun_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_immunization.write(code + " " + name + " " + code_system + "\n")
                fp_immunization.write(code_system + "\n")
        del code_list


def call_procedure(procedure_dict):
    '''
    procedure_dict: {"code": "90656", "name": "INFLUENZA VIRUS VACC SPLIT PRSRV FREE 3 YRS/> IM",
                        "code_system": "2.16.840.1.113883.6.12"}
    '''
    if fp_procedure is None:
        global fp_procedure
        fp_procedure = open("procedure.txt", 'a+b')
        code = unicode_OR_String(procedure_dict["code"])
        name = unicode_OR_String(procedure_dict["name"])
        code_system = unicode_OR_String(procedure_dict["code_system"])
        #fp_procedure.write(code + " " + name + " " + code_system + "\n")
        fp_procedure.write(code_system + "\n")
    else:
        fp_procedure.seek(0)
        file_content = fp_procedure.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(procedure_dict["code"])
        name = unicode_OR_String(procedure_dict["name"])
        code_system = unicode_OR_String(procedure_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_procedure.write(code + " " + name + " " + code_system + "\n")
                fp_procedure.write(code_system + "\n")
        del code_list


def call_problem(problem_dict):
    '''
    problem_dict: {"code_system_name": "SNOMED CT", "code": "44054006", "name": "Diabetes mellitus type 2 (disorder)",
    "code_system": "2.16.840.1.113883.6.96"}
    '''
    if fp_problem is None:
        global fp_problem
        fp_problem = open("problem.txt", 'a+b')
        code = unicode_OR_String(problem_dict["code"])
        name = unicode_OR_String(problem_dict["name"])
        code_system = unicode_OR_String(problem_dict["code_system"])
        code_system_name = unicode_OR_String(problem_dict["code_system_name"])
        #fp_problem.write(code + " " + name + " " + code_system + " " + code_system_name + "\n")
        fp_problem.write(code_system + " " + code_system_name + "\n")
    else:
        fp_problem.seek(0)
        file_content = fp_problem.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(problem_dict["code"])
        name = unicode_OR_String(problem_dict["name"])
        code_system = unicode_OR_String(problem_dict["code_system"])
        code_system_name = unicode_OR_String(problem_dict["code_system_name"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_problem.write(code + " " + name + " " + code_system + " " + code_system_name + "\n")
                fp_problem.write(code_system + " " + code_system_name + "\n")
        del code_list


def call_lab_code(lab_code_dict):
    '''
    {"code": "18719-5", "name": "", "code_system": "2.16.840.1.113883.6.1"}
    '''
    if fp_lab_code is None:
        global fp_lab_code
        fp_lab_code = open("lab_code.txt", 'a+b')
        code = unicode_OR_String(lab_code_dict["code"])
        name = unicode_OR_String(lab_code_dict["name"])
        code_system = unicode_OR_String(lab_code_dict["code_system"])
        #fp_lab_code.write(code + " " + name + " " + code_system + "\n")
        fp_lab_code.write(code_system + "\n")
    else:
        fp_lab_code.seek(0)
        file_content = fp_lab_code.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(lab_code_dict["code"])
        name = unicode_OR_String(lab_code_dict["name"])
        code_system = unicode_OR_String(lab_code_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_lab_code.write(code + " " + name + " " + code_system + "\n")
                fp_lab_code.write(code_system + "\n")
        del code_list


def call_lab_results(lab_result_dict):
    '''
    {"code": "6598-7","name": "TROPONIN T.CARDIAC:MCNC:PT:SER/PLAS:QN:", "code_system": "2.16.840.1.113883.6.1"}
    '''
    if fp_lab_result is None:
        global fp_lab_result
        fp_lab_result = open("lab_result.txt", 'a+b')
        code = unicode_OR_String(lab_result_dict["code"])
        name = unicode_OR_String(lab_result_dict["name"])
        code_system = unicode_OR_String(lab_result_dict["code_system"])
        #fp_lab_result.write(code + " " + name + " " + code_system + "\n")
        fp_lab_result.write(code_system + "\n")
    else:
        fp_lab_result.seek(0)
        file_content = fp_lab_code.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code = unicode_OR_String(lab_result_dict["code"])
        name = unicode_OR_String(lab_result_dict["name"])
        code_system = unicode_OR_String(lab_result_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_system not in code_list:
                #fp_lab_result.write(code + " " + name + " " + code_system + "\n")
                fp_lab_result.write(code_system + "\n")
        del code_list


def verify_dict_entry(Element, field, tag, input_dict):  # Access Value of a field, which is a dictionary
        if len(input_dict) == 0:
            logging.error("Testing for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_dict))
        else:
            for item in input_dict:
                if item == 'code':
                    if type(input_dict[item]) == dict:
                        ''' type(input_dict[item]) is dict for medications, immunizations and procedures '''
                        if input_dict[item]['code'] in ['', ' ', None]:
                            logging.error("Value for field: [%s] under <%s> ~ for value type %s", item, tag, type(input_dict[item]['code']))
                        else:
                            ''' Element like : 'medications' or 'immunizations' or 'problems' or 'labs' or 'procedures']'''
                            if Element == "medications":
                                call_medication(input_dict[item])
                            elif Element == "immunizations":
                                call_immunization(input_dict[item])
                            #elif Element == "procedures":
                                #call_procedure(input_dict[item])

                    else:
                        ''' type(input_dict[item]) is not dict for problems '''
                        if input_dict[item] in ['', ' ', None]:
                            logging.error("Value for field: [%s] under <%s> ~ for value type %s", item, tag, type(input_dict[item]))
                        else:
                            ''' Element like : 'medications' or 'immunizations' or 'problems' or 'labs' or 'procedures']'''
                            if Element == "problems":
                                call_problem(input_dict)
                            elif Element == "labs" and field == "code":
                                call_lab_code(input_dict)
                            elif Element == "labs" and field == "results":
                                call_lab_results(input_dict)
                            elif Element == "procedures":
                                call_procedure(input_dict)


def verify_list_entry(Element, field, tag, input_list):  # Access Value of a field, which is a list.
        if len(input_list) == 0:
            logging.error("Value for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_list))
        else:
            for i in range(len(input_list)):
                for item in input_list[i]:
                    if type(input_list[i][item]) == dict:  # In a list, value of a field as dictionary
                        str(tag).join(item)

                        verify_dict_entry(Element, field, tag, input_list[i][item])
                    else:
                        if item in ['unit']:
                            if input_list[i][item] in ['', ' ', None]:  # In a list, value of a field is a String
                                logging.error("Value for field: [%s] under <%s> ~ for value type %s", item, tag, type(input_list[i][item]))

                            else:
                                pass
                                #switch_method(input_list[i][item])


def _test_to_message(fp):
        """Verify CCDA document can be converted to a ProtoRPC message."""
        ccda_doc = ccda.CcdaDocument(fp)
        ccda_message = ccda_doc.to_message()
        #self.assertTrue(ccda_message, "ProtoRPC message is not successfully created")
    # TODO: Implement stronger test. Verify generated message against testdata.


def _test_to_json(fp):
        """Verify CCDA document can be converted to a JSON."""
        ccda_doc = ccda.CcdaDocument(fp)
        json_message = ccda_doc.to_json()
        #self.assertTrue(json_message, "JSON is not successfully created")

        # TODO: Implement stronger test. Verify generated message against testdata.
        JSON_file = json.loads(json_message)  # string complete_JSON to JSON file
        for elements in JSON_file:     # Each elements under json file, such as 'medication', 'vitals', 'labs' e.t.c
            if elements in ['medications', 'immunizations', 'problems', 'labs', 'procedures']:
                msg = "\n---Testing for " + elements + " from file " + str(fp.name) + "---"
                logging.info(msg)
                for entry in range(len(JSON_file[elements])):    # An entry is a dictionary from a list of entries (dictionaries) for elements
                    '''
                    JSON_file['medications'][0] =
                        {
                            "date_range": {},
                            "product": {
                                        "code": {"code": "311041", "name": "Insulin Glargine 100 UNT/ML Injectable Solution",
                                        "code_system": "2.16.840.1.113883.6.88"}
                                       },
                            "dose_quantity": {"unit": "1", "value": "30.0"}
                        }

                    JSON_file['labs'][0] =
                        {
                    {"code": {"code": ""},
                    "results": [{"date": "2013-01-24T13:12:12","code": {"code": "718-7", "name": "Hgb Bld-mCnc", "code_system": "2.16.840.1.113883.6.1"},
                                "unit": "g/dL", "value": "15.0"}]
                        }
                    '''
                    for key in JSON_file[elements][entry]:  # Key value is a name for each <name:value> in an entry
                        '''
                        key is "product" or "date_range" or "severity"
                        JSON_file['medications'][0]["product"] = {"code": {"code": "311041", "name": "Insulin Glargine 100 UNT/ML Injectable Solution",
                                                                         "code_system": "2.16.840.1.113883.6.88"}}
                        OR
                        key is "code" or "results"
                        JSON_file['labs'][0]["results"] = [{"date": "2013-01-24T13:12:12",
                                                            "code": {"code": "718-7", "name": "Hgb Bld-mCnc", "code_system": "2.16.840.1.113883.6.1"},
                                                            "unit": "g/dL", "value": "15.0"}]
                        JSON_file['labs'][0]["code"] = {"code": ""}
                        '''
                        if type(JSON_file[elements][entry][key]) == dict:
                            ''' elements like : 'medications' or 'immunizations' or 'problems' or 'procedures']'''
                            verify_dict_entry(elements, key, JSON_file[elements][entry], JSON_file[elements][entry][key])

                        elif type(JSON_file[elements][entry][key]) == list:
                            ''' elements like : 'labs' '''
                            verify_list_entry(elements, key, JSON_file[elements][entry], JSON_file[elements][entry][key])
                            ''' key is "code" or "results"  '''


def test_sample_ccda_files():
        """Test all sample CCDA files in the testdata directory."""
        count = 0
        for basename in os.listdir(TESTDATA_DIR):
            path = os.path.join(TESTDATA_DIR, basename)
            count = count + 1
            print path + ' --- start---- ' + str(count)
            #path = "/home/user/PycharmProjects/pyccda-master/testdata/multiple-bp.xml"
            fp = open(path)
            fp.seek(0)
            _test_to_message(fp)
            fp.seek(0)
            _test_to_json(fp)
            fp.close()
            print path + ' --- end---- ' + str(count)
            #path = "/home/user/PycharmProjects/pyccda-master/testdata/multiple-bp.xml"
            fp = open(path)
            fp.seek(0)
            _test_to_message(fp)
            fp.seek(0)
            _test_to_json(fp)
            fp.close()

#if __name__ == '__main__':
test_sample_ccda_files()
