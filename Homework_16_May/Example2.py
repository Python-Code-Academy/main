
class StringClass:
    def __init__(self):
        self.input_str = self.getString()
    
    
    def getString(self):
        return input("Please insert some text:")
         

    def printString(self):
        print(self.input_str.upper())
        return(self.input_str.upper())
#     def __init__(self):
#         self.input_str = self.getString()
#
#     def getString(self):
#         self.input_str = input("Please insert some text.\n")
#
#         return self.input_str
#
#     def printString(self):
#         result = self.input_str.upper()
#
#         print(result)
#
#         return result
#
#
# #calling class ConvertUpperCase
# convert_object = ConvertUpperCase()
# result = convert_object.printString()