"""Unit tests for ccda.py."""

import ccda
import os
import unittest
import json
import logging

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), '../testdata')
logging.basicConfig(filename='test.log', filemode='w', format='%(asctime)s--%(levelname)s:--%(message)s',
                        level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %P')

class CcdaDocumentTestCase(unittest.TestCase):
  #def _test_to_csv(self, fp):
  #  """Verify CCDA document can be converted to a CSV file."""
  #  ccda_doc = ccda.CcdaDocument(fp)
  #  ccda_csv = ccda_doc.to_csv()
  #  self.assertTrue(ccda_csv)
  # TODO: Implement stronger test. Verify generated CSV against testdata.

    def verify_dict_entry(self, field, input_dict):  # Access Value of a field, which is a dictionary
        if len(input_dict) == 0:
            logging.error("Testing for field: [%s] with value type %s", field, type(input_dict))
        else:
            for item in input_dict:
                if input_dict[item] in ['', ' ', None]:
                    logging.error("Testing for field: [%s] with value type %s", item, type(input_dict[item]))

    def verify_list_entry(self, field, input_list):  # Access Value of a field, which is a list.
        if len(input_list) == 0:
            logging.error("Testing for field: [%s] with value type %s", field, type(input_list))
        else:
            for i in range(len(input_list)):
                for item in input_list[i]:
                    if type(input_list[i][item]) == dict:  # In a list, value of a field as dictionary
                        self.verify_dict_entry(item, input_list[i][item])
                    else:
                        if input_list[i][item] in ['', ' ', None]:  # In a list, value of a field is a String
                            logging.error("Testing for field: [%s] with value type %s", item, type(input_list[i][item]))

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
            if elements not in ['demographics', 'social', 'encounter']:
                msg = "---Testing for " + elements + " from file " + str(fp.name) + "---"
                logging.info(msg)
                for entry in range(len(JSON_file[elements])):    # entry stands for a dictionary from a list of dictionaries for elements
                    for key in JSON_file[elements][entry]:

                        if type(JSON_file[elements][entry][key]) == dict:
                            self.verify_dict_entry(key, JSON_file[elements][entry][key])

                        elif type(JSON_file[elements][entry][key]) == list:
                            self.verify_list_entry(key, JSON_file[elements][entry][key])
                        else:
                            if JSON_file[elements][entry][key] in ['', ' ', None]:
                                logging.error("Testing for field: [%s] with value type %s", key, JSON_file[elements][entry][key])

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
