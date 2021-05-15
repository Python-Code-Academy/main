class InvalidItemType(Exception):
    # print("Invalid item type.")
    def __init__(self, message = "Invalid item type."):
        self.message = message 
  
<<<<<<< HEAD
    
=======
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
    def __str__(self):
        if (self.message):
            return self.message
        else:
            return "Invalid item type error has been raised."

class ItemNotLocked(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OutOfStock(Exception):
    def __init__(self, message="Product is out of stock."):
        self.message = message
        super().__init__(self.message)