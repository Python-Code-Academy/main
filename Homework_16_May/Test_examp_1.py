"""
    Write a function, which will find all such numbers between 200 and 300
    (both included) such that each digit of the number is an even number.
    
    The numbers obtained should be printed in a csv sequence on a single line.
    
    Create unit test to test the function.
"""

from Example1 import EvenNums
import unittest
import sys
from io import StringIO


class TestEvenNumbers(unittest.TestCase):

    def setUp(self):
        self.list1 = EvenNums(200,240)
    
    # In case the print_even_numbers() function returns a list we should use this test 
    # def test_print_even_numbers(self):
    #     result = self.list1.print_even_numbers()
    #     expected_list = [200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240]
    #     negative_test_list = [200, 202, 204, 227, 206, 208, 210, 220, 222, 224, 226, 228, 240]
    #     self.assertEqual(result, expected_list) 
    #     self.assertNotEqual(result, negative_test_list)  

    # In case the print_even_numbers() function prints the numbers we use the following test
    def test_print_even_numbers(self):
        expected = "200,202,204,206,208,220,222,224,226,228,240"
        capturedOutput = StringIO()          # Create StringIO object
        sys.stdout = capturedOutput          #  and redirect stdout.
        self.list1.print_even_numbers()      # Call unchanged function.
        sys.stdout = sys.__stdout__          # Reset redirect.
        self.assertEqual(expected, capturedOutput.getvalue())
        
        
if __name__ == "__main__":
    unittest.main()
    