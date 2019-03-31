import HtmlTestRunner
import unittest
from Test1 import Test1

class SimpleTest(unittest.TestCase):

    # Returns True or False.  
    def test(self):
        inst = Test1()
        self.assertEquals(10,inst.method1())

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False))
