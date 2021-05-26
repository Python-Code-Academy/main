'''
Write a TDD based test for a class with method calcFreq() that compute the frequency of words in string entered from the console input.
Prepare a second test with patch for calcFreq() and execute the patched test.
The output should output after sorting the key alphanumerically.
Test data: I felt happy because I saw the others were happy and because I knew I should feel happy, but I was not really happy.  24
[2,1,
{'I': 5, 'and': 1, 'because': 2, 'but': 1,  'feel': 1, 'felt': 1, 'happy': 4, 'knew': 1, 'not': 1, 'others': 1, 'really': 1, 'saw': 1, 'should': 1, 'the' : 1,
'was': 1, 'were': 1}



Hints In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import unittest
from .String import CalcString

class TestCalcString(unittest.TestCase):
    def setUp(self):
        self.str_class = CalcString()
    
    def test_calcFreq(self):
        expected_dict = {'I': 5, 'and': 1, 'because': 2, 'but': 1,  'feel': 1, 'felt': 1, 'happy': 4, 'knew': 1, 'not': 1, 'others': 1, 'really': 1, 'saw': 1, 'should': 1, 'the' : 1, 'was': 1, 'were': 1}
        self.assertEqual(expected_dict, self.str_class.calcFreq())
    
if __name__ == '__main__':
    unittest.main()
    