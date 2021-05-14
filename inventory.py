from custom_exceptions import *

class Inventory:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item_name, quantity):
        if type(item_name) is not str:
            raise ValueError("Item name must be a string.")
        
        if type(quantity) is not int or quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        
        self.items[item_name] = Item(item_name)
        self.items[item_name] = quantity
        
    
    def lock(self, item_type):
        '''Select the type of item that is going to be manipulated.
        This method will lock the item so nobody else can manipulate
        the inventory until it's returned. This prevents selling the
        same item to two different customers '''
        if(item_type in self.items.keys() and self.items.get(item_type > 0)):
            return True
        else:
            return False:
        #item_type.locked = True
        #pass
    
    def unlock(self, item_type):
        '''Release the given type so that other customers can access it.'''
        pass
    
    def purchase(self, item_type):
        '''If the item is not locked, raise an exception.
        If the item type does not exist, raise an exception. 
        If the item is currently out of stock, raise an exception.
        If the item is available, substract one item and return the number
        of items left.'''
        if(item_type not in self.items.keys()):
            raise InvalidItemType  
        
        item_quantity = self.items.get(item_type)
        
        if (item_quantity <= 0):
            raise OutOfStock
        else:
            item_quantity -= 1
        
        return item_quantity
        
        
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.locked = False
        self.quantity = quantity


inv1 = Inventory()
inv1.add_item("iphone", 3)
inv1.add_item("samsung", 0)

item_type = 'iphone'

inv1.lock(item_type)

try:
    num_left = inv1.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, the item is out of stock.")
else:
    print("Purchase complete. There are {} {}s left".format(num_left, item_type))
finally:
    inv1.unlock(item_type)