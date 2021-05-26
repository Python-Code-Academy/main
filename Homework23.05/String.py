import re

class CalcString:
    def __init__(self):
        self.str = input("Please insert some text: ")
        

    def calcFreq(self):
        words = {}
        ls = re.findall(r"[\w']+", self.str)
        
        for word in ls:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        
        return dict(sorted(words.items()))
