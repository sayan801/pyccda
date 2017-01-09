"""Unit tests for ccda.py."""

import ccda
import os
import unittest
import json
import logging

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), '../testdata')
logging.basicConfig(filename='Vitals_test.log', filemode='w', format='%(asctime)s--%(levelname)s:--%(message)s',
                        level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %P')
vital_code = None
vital_dict = {"Height": None, "Height_lying": None, "BMI": None, "BP_Diastolic": None, "BP_Systolic": None,
              "Weight": None, "Temperature": None, "Heart_Rate": None, "Respiratory Rate": None,
              "Oxygen_Saturation": None}


class CcdaDocumentTestCase(unittest.TestCase):
  #def _test_to_csv(self, fp):
  #  """Verify CCDA document can be converted to a CSV file."""
  #  ccda_doc = ccda.CcdaDocument(fp)
  #  ccda_csv = ccda_doc.to_csv()
  #  self.assertTrue(ccda_csv)
  # TODO: Implement stronger test. Verify generated CSV against testdata.

    def switch_method(self, code, unit):
        if code in ['39156-5', '41909-3']:   # BMI
            if vital_dict['BMI'] is None:
                file_name = 'BMI' + ".txt"
                vital_dict['BMI'] = open(file_name, "a+b")
            else:
                vital_dict['BMI'].seek(0)
                file_content = vital_dict['BMI'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['BMI'].write(unit + "\n")

        elif code in ['8302-2']:   # height
            if vital_dict['Height'] is None:
                file_name = 'Height' + ".txt"
                vital_dict['Height'] = open(file_name, "a+b")
            else:
                vital_dict['Height'].seek(0)
                file_content = vital_dict['Height'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Height'].write(unit + "\n")

        elif code in ['8306-3']:   # height lying
            if vital_dict['Height_lying'] is None:
                file_name = 'Height_lying' + ".txt"
                vital_dict['Height_lying'] = open(file_name, "a+b")
            else:
                vital_dict['Height_lying'].seek(0)
                file_content = vital_dict['Height_lying'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Height_lying'].write(unit + "\n")

        elif code in ['3141-9']:   # weight
            if vital_dict['Weight'] is None:
                file_name = 'Weight' + ".txt"
                vital_dict['Weight'] = open(file_name, "a+b")
            else:
                vital_dict['Weight'].seek(0)
                file_content = vital_dict['Weight'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Weight'].write(unit + "\n")

        elif code in ['8310-5']:   # Temperature
            if vital_dict['Temperature'] is None:
                file_name = 'Temperature' + ".txt"
                vital_dict['Temperature'] = open(file_name, "a+b")
            else:
                vital_dict['Temperature'].seek(0)
                file_content = vital_dict['Temperature'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Temperature'].write(unit + "\n")

        elif code in ['8867-4']:   # heart_rate
            if vital_dict['Heart_Rate'] is None:
                file_name = 'Heart_Rate' + ".txt"
                vital_dict['Heart_Rate'] = open(file_name, "a+b")
            else:
                vital_dict['Heart_Rate'].seek(0)
                file_content = vital_dict['Heart_Rate'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Heart_Rate'].write(unit + "\n")

        elif code in ['59408-5']:   # Oxygen_Saturation
            if vital_dict['Oxygen_Saturation'] is None:
                file_name = 'Oxygen_Saturation' + ".txt"
                vital_dict['Oxygen_Saturation'] = open(file_name, "a+b")
            else:
                vital_dict['Oxygen_Saturation'].seek(0)
                file_content = vital_dict['Oxygen_Saturation'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Oxygen_Saturation'].write(unit + "\n")

        elif code in ['9279-1']:   # Resp_rate
            if vital_dict['Respiratory Rate'] is None:
                file_name = 'Respiratory Rate' + ".txt"
                vital_dict['Respiratory Rate'] = open(file_name, "a+b")
            else:
                vital_dict['Respiratory Rate'].seek(0)
                file_content = vital_dict['Respiratory Rate'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['Respiratory Rate'].write(unit + "\n")

        elif code in ['8462-4']:   # bp_diastolic
            if vital_dict['BP_Diastolic'] is None:
                file_name = 'BP_Diastolic' + ".txt"
                vital_dict['BP_Diastolic'] = open(file_name, "a+b")
            else:
                vital_dict['BP_Diastolic'].seek(0)
                file_content = vital_dict['BP_Diastolic'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['BP_Diastolic'].write(unit + "\n")

        elif code in ['8480-6']:   # bp_systolic
            if vital_dict['BP_Systolic'] is None:
                file_name = 'BP_Systolic' + ".txt"
                vital_dict['BP_Systolic'] = open(file_name, "a+b")
            else:
                vital_dict['BP_Systolic'].seek(0)
                file_content = vital_dict['BP_Systolic'].readlines()
                for element in file_content:
                    file_content[file_content.index(element)] = element.strip('\n')
                    print vital_field
                    if unit not in file_content:
                        vital_dict['BP_Systolic'].write(unit + "\n")

    def verify_dict_entry(self, field, tag, input_dict):  # Access Value of a field, which is a dictionary
        if len(input_dict) == 0:
            logging.error("Testing for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_dict))
        else:
            for item in input_dict:
                if item == 'code':
                    if input_dict[item] in ['', ' ', None]:
                        logging.error("Value for field: [%s] under <%s> ~ for value type %s", item, tag, type(input_dict[item]))
                        global vital_code
                        vital_code = None
                    else:
                        global vital_code
                        vital_code = input_dict[item]
                        '''if vital_field in ["Body Mass Index", "Body Height (Measured)", "Body Weight (Measured)", "BMI (Body Mass Index)",
                                           "SYSTOLIC BLOOD PRESSURE", "DIASTOLIC BLOOD PRESSURE", "HEART RATE"]:'''
                        self.switch_method(vital_code, 0)


                        logging.info("Field is : %s  ", vital_code)

    def verify_list_entry(self, field, tag, input_list):  # Access Value of a field, which is a list.
        if len(input_list) == 0:
            logging.error("Value for field: [%s] under <%s> ~ for value type %s", field, tag, type(input_list))
        else:
            for i in range(len(input_list)):
                for item in input_list[i]:
                    if type(input_list[i][item]) == dict:  # In a list, value of a field as dictionary
                        str(tag).join(item)

                        self.verify_dict_entry(item, tag, input_list[i][item])
                    else:
                        if item in ['unit']:
                            if input_list[i][item] in ['', ' ', None]:  # In a list, value of a field is a String
                                logging.error("Value for field: [%s] under <%s> ~ for value type %s", item, tag, type(input_list[i][item]))

                            else:
                                self.switch_method(vital_code, input_list[i][item])
                                '''if vital_field is not None:
                                    logging.info("%s unit is = %s  ", vital_field, input_list[i][item])
                                    vital_dict[vital_field].seek(0)
                                    file_content = vital_dict[vital_field].readlines()
                                    for element in file_content:
                                        file_content[file_content.index(element)] = element.strip('\n')
                                    if input_list[i][item] not in file_content and vital_field not in ["Body Mass Index", "Body Height (Measured)",
                                                                                                       "Body Weight (Measured)", "BMI (Body Mass Index)",
                                                                                                       "SYSTOLIC BLOOD PRESSURE", "DIASTOLIC BLOOD PRESSURE",
                                                                                                       "HEART RATE"]:
                                        print vital_field
                                        vital_dict[vital_field].write(input_list[i][item] + "\n")'''

    def _test_to_message(self, fp):
        """Verify CCDA document can be converted to a ProtoRPC message."""
        ccda_doc = ccda.CcdaDocument(fp)
        ccda_message = ccda_doc.to_message()
        self.assertTrue(ccda_message, "ProtoRPC message is not successfully created")
    # TODO: Implement stronger test. Verify generated message against testdata.

    def _test_to_json(self, fp):
        """Verify CCDA document can be converted to a JSON."""
        ccda_doc = ccda.CcdaDocument(fp)
        json_message = ccda_doc.to_json()
        self.assertTrue(json_message, "JSON is not successfully created")

        # TODO: Implement stronger test. Verify generated message against testdata.
        JSON_file = json.loads(json_message)  # string complete_JSON to JSON file
        for elements in JSON_file:     # Each elements under json file, such as 'medication', 'vitals', 'labs' e.t.c
            if elements in ['vitals']:
                msg = "\n---Testing for " + elements + " from file " + str(fp.name) + "---"
                logging.info(msg)
                for entry in range(len(JSON_file[elements])):    # An entry is a dictionary from a list of entries (dictionaries) for elements
                    for key in JSON_file[elements][entry]:  # Key value is a name for each <name:value> in an entry

                        global vital_field
                        vital_field = None
                        
                        if type(JSON_file[elements][entry][key]) == dict:
                            self.verify_dict_entry(key, JSON_file[elements][entry], JSON_file[elements][entry][key])

                        elif type(JSON_file[elements][entry][key]) == list:
                            self.verify_list_entry(key, JSON_file[elements][entry], JSON_file[elements][entry][key])
                        else:
                            if JSON_file[elements][entry][key] in ['', ' ', None]:
                                logging.error("Value for field: [%s] under <%s> ~ for value type %s", key, JSON_file[elements][entry],
                                              type(JSON_file[elements][entry][key]))
                                '''global vital_field
                                vital_field = None'''

    def test_sample_ccda_files(self):
        """Test all sample CCDA files in the testdata directory."""
        count = 0
        for basename in os.listdir(TESTDATA_DIR):
            path = os.path.join(TESTDATA_DIR, basename)
            count = count + 1
            print path + ' --- start---- ' + str(count)
            #path = "/home/user/PycharmProjects/pyccda-master/testdata/multiple-bp.xml"
            fp = open(path)
            fp.seek(0)
            self._test_to_message(fp)
            fp.seek(0)
            self._test_to_json(fp)
            fp.close()
            print path + ' --- end---- ' + str(count)
            #path = "/home/user/PycharmProjects/pyccda-master/testdata/multiple-bp.xml"
            fp = open(path)
            fp.seek(0)
            self._test_to_message(fp)
            fp.seek(0)
            self._test_to_json(fp)
            fp.close()

if __name__ == '__main__':
  unittest.main()
