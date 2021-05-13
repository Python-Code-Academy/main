class InvalidItemType(Exception):
    # print("Invalid item type.")
    def __init__(self):
        super().__init__()



class OutOfStock(Exception):
    def __init__(self):
        super().__init__()