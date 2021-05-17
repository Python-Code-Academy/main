"""
    1.Create TDD based unit test which test 2 methods-
    getString() and printString() who convert lowercases string and to print uppercases string
    
    3.Define a class which has at least two methods:
    getString(): to get a string from console input
    and printString(): to print the string in uppercases
    
    Hint:
     Use init method to construct some parameters
     Create unit test to test the method in the class.
"""

from Example2 import StringClass
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):   
        self.str_class = StringClass()
        
    def test_getString(self):
        self.assertEqual("vw", self.str_class.input_str)
    

    def test_printString(self):
        self.assertEqual("VW", self.str_class.printString())

    
if __name__ == "__main__":
    unittest.main()
    
    