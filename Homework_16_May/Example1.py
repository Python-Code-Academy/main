class EvenNums():
    
    def __init__(self, x, y):
        self.list1 = []
        for num in range(x, y + 1):
            self.list1.append(num)
    
    def print_even_numbers(self):
        result = []

        for num in self.list1:
            firstDigit = int(num / 100)
            secondDigit = int((num / 10) % 10)
            lastDigit = int(num % 10)
            if(firstDigit % 2 == 0 and secondDigit % 2 == 0 and lastDigit % 2 == 0):
                result.append(num)
        
        for n in result:
            if n != result[-1]:
                print(n, end = ",")
            else:
                print(n, end = "")
        # Uncomment this so the fun returns a list
        # return result

even = EvenNums(200, 240)
even.print_even_numbers()