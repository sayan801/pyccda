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
fp_reaction = None
fp_severity = None
fp_name = None

#class CcdaDocumentTestCase(unittest.TestCase):
  #def _test_to_csv(self, fp):
  #  """Verify CCDA document can be converted to a CSV file."""
  #  ccda_doc = ccda.CcdaDocument(fp)
  #  ccda_csv = ccda_doc.to_csv()
  #  self.assertTrue(ccda_csv)
  # TODO: Implement stronger test. Verify generated CSV against testdata.


def unicode_OR_String(variable):
    if isinstance(variable, unicode):
        return variable.encode('utf-8')
    elif isinstance(variable, str):
        return variable


def call_reaction(react_dict):
    '''
    react_dict: {"code_system_name": "SNOMED CT", "code": "422587007", "name": "Nausea (finding)","code_system": "2.16.840.1.113883.6.96"}
    '''

    if fp_reaction is None:
        global fp_reaction
        fp_reaction = open("allergy_reaction.txt", 'a+b')
        code_name = unicode_OR_String(react_dict["code_system_name"])
        code_ID = unicode_OR_String(react_dict["code_system"])
        fp_reaction.write(code_ID + " " + code_name + "\n")
    else:
        fp_reaction.seek(0)
        file_content = fp_reaction.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code_name = unicode_OR_String(react_dict["code_system_name"])
        code_ID = unicode_OR_String(react_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][1] not in code_list:
                code_list.append(file_content[i][0])
        if code_ID not in code_list:
                fp_reaction.write(code_ID + " " + code_name + "\n")
        del code_list


def call_severity(sever_dict):
    '''
    sever_dict: {"code_system_name": "SNOMED CT", "code": "6736007", "name": "", "code_system": "2.16.840.1.113883.6.96"}
    '''
    if fp_severity is None:
        global fp_severity
        fp_severity = open("allergy_severity.txt", 'a+b')
        code_name = unicode_OR_String(sever_dict["code_system_name"])
        code_ID = unicode_OR_String(sever_dict["code_system"])
        fp_severity.write(code_ID + " " + code_name + "\n")
    else:
        fp_severity.seek(0)
        file_content = fp_severity.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code_name = unicode_OR_String(sever_dict["code_system_name"])
        code_ID = unicode_OR_String(sever_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][1] not in code_list:
                code_list.append(file_content[i][0])
        if code_ID not in code_list:
                fp_severity.write(code_ID + " " + code_name + "\n")
        del code_list


def call_name(name_dict):
    '''
    code_dict: {"code_system_name": "RxNorm", "code": "2670", "name": "Codeine","code_system": "2.16.840.1.113883.6.88"}
    '''
    if fp_name is None:
        global fp_name
        fp_name = open("allergy_name.txt", 'a+b')
        code_name = unicode_OR_String(name_dict["code_system_name"])
        code_ID = unicode_OR_String(name_dict["code_system"])
        fp_name.write(code_ID + " " + code_name + "\n")
    else:
        fp_name.seek(0)
        file_content = fp_name.readlines()
        for element in file_content:
            file_content[file_content.index(element)] = element.strip('\n')
        for element in file_content:
            file_content[file_content.index(element)] = element.split(' ')
        code_name = unicode_OR_String(name_dict["code_system_name"])
        code_ID = unicode_OR_String(name_dict["code_system"])

        code_list = list()
        for i in range(len(file_content)):
            if file_content[i][0] not in code_list:
                code_list.append(file_content[i][0])
        if code_ID not in code_list:
                fp_name.write(code_ID + " " + code_name + "\n")
        del code_list


def verify_dict_entry(field, tag, input_dict):  # Access Value of a field, which is a dictionary
        if len(input_dict) == 0:
            logging.error("Testing for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_dict))
        else:
            if field == "reaction":
                if input_dict["code_system_name"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system_name", tag, type(input_dict["code_system_name"]))
                elif input_dict["code_system"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system", tag, type(input_dict["code_system"]))
                if input_dict["code_system"] not in ['', ' ', None] and input_dict["code_system_name"] not in ['', ' ', None]:
                    call_reaction(input_dict)

            elif field == "severity":
                if input_dict["code_system_name"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system_name", tag, type(input_dict["code_system_name"]))
                elif input_dict["code_system"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system", tag, type(input_dict["code_system"]))
                if input_dict["code_system"] not in ['', ' ', None] and input_dict["code_system_name"] not in ['', ' ', None]:
                    call_severity(input_dict)

            else:
                if input_dict["code_system_name"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system_name", tag, type(input_dict["code_system_name"]))
                elif input_dict["code_system"] in ['', ' ', None]:
                    logging.error("Value for field: [%s] under <%s> ~ for value type %s", "code_system", tag, type(input_dict["code_system"]))
                if input_dict["code_system"] not in ['', ' ', None] and input_dict["code_system_name"] not in ['', ' ', None]:
                    call_name(input_dict)


def verify_list_entry(field, tag, input_list):  # Access Value of a field, which is a list.
        if len(input_list) == 0:
            logging.error("Value for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_list))
        else:
            for i in range(len(input_list)):
                for item in input_list[i]:
                    if type(input_list[i][item]) == dict:  # In a list, value of a field as dictionary
                        str(tag).join(item)

                        verify_dict_entry(item, tag, input_list[i][item])
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
            if elements in ['allergies']:
                msg = "\n---Testing for " + elements + " from file " + str(fp.name) + "---"
                logging.info(msg)
                for entry in range(len(JSON_file[elements])):    # An entry is a dictionary from a list of entries (dictionaries) for elements
                    '''
                    { JSON_file['allergies'][0] =
        "reaction": {"code_system_name": "SNOMED CT", "code": "422587007", "name": "Nausea (finding)","code_system": "2.16.840.1.113883.6.96"},
        "code": {"code_system_name": "RxNorm", "code": "2670", "name": "Codeine","code_system": "2.16.840.1.113883.6.88"},
        "severity": {"code_system_name": "SNOMED CT", "code": "6736007", "name": "", "code_system": "2.16.840.1.113883.6.96"}
                    }
                    '''
                    for key in JSON_file[elements][entry]:  # Key value is a name for each <name:value> in an entry
                        '''
                        key is "reaction" or "code" or "severity"
                        JSON_file['allergies'][0]["reaction"] ={"code_system_name": "SNOMED CT", "code": "422587007",
                                                                "name": "Nausea (finding)","code_system": "2.16.840.1.113883.6.96"}
                        '''
                        if type(JSON_file[elements][entry][key]) == dict:
                            verify_dict_entry(key, JSON_file[elements][entry], JSON_file[elements][entry][key])

                        '''elif type(JSON_file[elements][entry][key]) == list:
                            verify_list_entry(key, JSON_file[elements][entry], JSON_file[elements][entry][key])
                        else:
                            if JSON_file[elements][entry][key] in ['', ' ', None]:
                                logging.error("Value for field: [%s] under <%s> ~ for value type %s", key, JSON_file[elements][entry],
                                              type(JSON_file[elements][entry][key]))'''


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
