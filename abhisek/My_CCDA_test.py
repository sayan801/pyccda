import sys
import unittest
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestCase(unittest.TestCase):
    def testSimpleMsg(self):
        stream_handler.stream = sys.stdout
        print("AA")
        logging.getLogger().info("BB")


'''import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')'''