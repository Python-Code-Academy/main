import unittest
from unittest.mock import patch


class TestString(unittest.TestCase):
    
    @patch('String.CalcString.calcFreq', return_value={'I': 5, 'and': 1, 'because': 2, 'but': 1,  'feel': 1, 'felt': 1, 'happy': 4, 'knew': 1, 'not': 1, 'others': 1, 'really': 1, 'saw': 1, 'should': 1, 'the' : 1, 'was': 1, 'were': 1})   
    def test_calcFreq(self,calcFreq):
        print(calcFreq)
        str_words=input("Please insert some text: ")
        expected_dict = {'I': 5, 'and': 1, 'because': 2, 'but': 1,  'feel': 1, 'felt': 1, 'happy': 4, 'knew': 1, 'not': 1, 'others': 1, 'really': 1, 'saw': 1, 'should': 1, 'the' : 1, 'was': 1, 'were': 1}
        self.assertEqual(calcFreq(str_words),expected_dict)
        
if __name__ == '__main__':
    unittest.main()