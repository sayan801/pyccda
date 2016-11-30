"""Unit tests for ccda.py."""

import ccda
import os
import unittest

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), '../testdata')


class CcdaDocumentTestCase(unittest.TestCase):

  #def _test_to_csv(self, fp):
  #  """Verify CCDA document can be converted to a CSV file."""
  #  ccda_doc = ccda.CcdaDocument(fp)
  #  ccda_csv = ccda_doc.to_csv()
  #  self.assertTrue(ccda_csv)
  # TODO: Implement stronger test. Verify generated CSV against testdata.

  def _test_to_message(self, fp):
    """Verify CCDA document can be converted to a ProtoRPC message."""
    ccda_doc = ccda.CcdaDocument(fp)
    ccda_message = ccda_doc.to_message()
    self.assertTrue(ccda_message)
    # TODO: Implement stronger test. Verify generated message against testdata.

  def test_sample_ccda_files(self):
    """Test all sample CCDA files in the testdata directory."""
    count = 0 
    for basename in os.listdir(TESTDATA_DIR):	
      path = os.path.join(TESTDATA_DIR, basename)
      count = count + 1
      print path + ' --- start---- ' + str(count)
      fp = open ( path ) 
      fp.seek(0)
      self._test_to_message(fp)
      fp.close()
      print path + ' --- end---- '  + str(count)


if __name__ == '__main__':
  unittest.main()
