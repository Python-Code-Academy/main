from custom_exceptions import *

<<<<<<< HEAD
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
=======
class Item:            
    def __init__(self, name, quantity):
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        self.set_name(name)
        self.set_quantity(quantity)
        self.locked = False
        
    def __str__(self):
<<<<<<< HEAD
        """
        Prints name of item stack
        """
        return self.name

    def set_name(self, name):
        """
        Set the name of the item stack
        """
=======
        return self.name

    def set_name(self, name):
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        if(type(name)is not str):
            raise ValueError("Name must be a string")
        else:
            self.name = name
           
    def set_quantity(self, quantity):
<<<<<<< HEAD
        """
        Set the number of items in the stack
        """
=======
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        if(type(quantity) is not int or quantity < 0):
            raise ValueError("Quantity must be a positive integer")
        else:
            self.quantity = quantity
<<<<<<< HEAD
            
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
=======
    
    def take_item(self):
        if (self. quantity > 0):
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
            self.quantity -= 1
        else:
            raise OutOfStock
        
<<<<<<< HEAD
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
=======
class Inventory:
    def __init__(self):
        self.items = {}
    
    def item_exists(self, item):
        return item in self.items
    
    def is_locked(self, item):
        return self.items[item].locked
    
    def add_item(self, itemToAdd):
        if (self.item_exists(itemToAdd)):
            existing_item = self.items[itemToAdd.name]
            existing_item.quantity += itemToAdd.quantity
        else: 
            if type(itemToAdd) is not Item:
                raise InvalidItemType()
            self.items[itemToAdd] = itemToAdd
        
    def lock(self, item):
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        if (self.item_exists(item)):
            self.items[item].locked = True
        else:
            raise InvalidItemType()
    
    def unlock(self, item):
<<<<<<< HEAD
        """
        Unlocks an item stack if it exists in the inventory.
        """
=======
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        if (self.item_exists(item)):
            self.items[item].locked = False

    def validate_purchase(self, item):
<<<<<<< HEAD
        """
        If the item type does not exist, raise an exception.
        If the item is not locked, raise an exception. 
        If the item is currently out of stock, raise an exception.
        If the item is available, substract one item and return the number
        of items left
        """
=======
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        if (not self.item_exists(item)):
            raise InvalidItemType
        elif item.locked == False:
            raise ItemNotLocked
<<<<<<< HEAD
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
=======
        elif self.items[item].quantity <= 0:
            raise OutOfStock
        else:
            self.items[item].take_item()
        return self.items[item].quantity
    
    def buy_item(self, item):
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
        try:
            self.lock(item)
            num_left = self.validate_purchase(item)
        except InvalidItemType:
            print("Sorry, we don't sell {}".format(str(item)))
        except OutOfStock:
            print("Sorry, the item is out of stock.")
        else:
<<<<<<< HEAD
            print("Purchase complete. There are {} {}s left".format(num_left, item.get_name()))
        finally:
            self.unlock(item)
        
=======
            print("Purchase complete. There are {} {}s left".format(num_left, item.name))
        finally:
            self.unlock(item)
        
iphones = Item("iPhone", 2)
samsung_phones = Item("Samsung", 11)
item1 = Item("item1", 2)

online_store = Inventory()
online_store.add_item(iphones)
online_store.add_item(samsung_phones)
online_store.buy_item(iphones)
online_store.buy_item(iphones)
online_store.buy_item(samsung_phones)
online_store.buy_item("jfdkdsk")
online_store.buy_item(item1)
>>>>>>> 4a65d26b1ef3f37d3a9c9b6d7adaa316a9658422
