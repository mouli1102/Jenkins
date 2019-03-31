import unittest 
import requests

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        inst = requests.get("http://localhost:5009/")
        self.assertEquals(22,int(inst.text) )
  
if __name__ == '__main__': 
    unittest.main() 
