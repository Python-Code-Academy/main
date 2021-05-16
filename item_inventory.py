from custom_exceptions import *

class Item:   
    """
    A class that represents a group of items in our store.
    
    Attributes
    -----
    name : name of item stack 
    quantity : number of items in the stack
    locked : is the stack locked or not
    """    
    def __init__(self, name, quantity):
        """
        Initialize the attributes name and quantity 
        """
        self.set_name(name)
        self.set_quantity(quantity)
        self.locked = False
        
    def __str__(self):
        """
        Prints name of item stack
        """
        return self.name

    def set_name(self, name):
        """
        Set the name of the item stack
        """
        if(type(name)is not str):
            raise ValueError("Name must be a string")
        else:
            self.name = name
           
    def set_quantity(self, quantity):
        """
        Set the number of items in the stack
        """
        if(type(quantity) is not int or quantity < 0):
            raise ValueError("Quantity must be a positive integer")
        else:
            self.quantity = quantity
            
    def get_name(self):
        """
        Returns the item stack name
        """
        return self.name
    
    def get_quantity(self):
        """
        Returns the number of items in the stack
        """
        return self.quantity
    
    def take_item(self):
        """
        Removes 1 item from the item stack.
        Raises OutOfStock error if there are no items left.
        """
        if (self.quantity > 0):
            self.quantity -= 1
        else:
            raise OutOfStock
        
    def restock_item(self, quantity):
        """
        Adds the provided quantity parameter to the overall quantity in the item stack.
        """
        self.quantity += quantity
    
class Inventory:
    """
    A class that represents an inventory (for an online shop or company).
    """
    def __init__(self):
        """
        Initializes an empty dictionary to store the item stacks
        """
        self.items = {}
    
    def item_exists(self, item):
        """
        Checks if the item is present in the inventory.
        """
        return item in self.items
    
    def add_item(self, item_to_add):
        """
        Re-stocks the item if it exists in the inventory.
        Else adds the item in the inventory.
        Raises an exception if provided with invalid input.
        """
        if (self.item_exists(item_to_add)):
            existing_item = self.items[item_to_add.get_name()]
            existing_item.restock_item(item_to_add.get_quantity())
        else: 
            if type(item_to_add) is not Item:
                raise InvalidItemType()
            self.items[item_to_add] = item_to_add
        
    def lock(self, item):
        """
        Locks an item stack if it exists in the inventory.
        Else raise an InvalidItemType exception.
        """
        if (self.item_exists(item)):
            self.items[item].locked = True
        else:
            raise InvalidItemType()
    
    def unlock(self, item):
        """
        Unlocks an item stack if it exists in the inventory.
        """
        if (self.item_exists(item)):
            self.items[item].locked = False

    def validate_purchase(self, item):
        """
        If the item type does not exist, raise an exception.
        If the item is not locked, raise an exception. 
        If the item is currently out of stock, raise an exception.
        If the item is available, substract one item and return the number
        of items left
        """
        if (not self.item_exists(item)):
            raise InvalidItemType
        elif item.locked == False:
            raise ItemNotLocked
        elif self.items[item].get_quantity() <= 0:
            raise OutOfStock
        else:
            self.items[item].take_item()
        return self.items[item].get_quantity()
    
    def buy_item(self, item):
        """
        Lock the item and call validate_purchase().
        Handle possible exceptions.
        Unlocks the item.
        """
        try:
            self.lock(item)
            num_left = self.validate_purchase(item)
        except InvalidItemType:
            print("Sorry, we don't sell {}".format(str(item)))
        except OutOfStock:
            print("Sorry, the item is out of stock.")
        else:
            print("Purchase complete. There are {} {}s left".format(num_left, item.get_name()))
        finally:
            self.unlock(item)
