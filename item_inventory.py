from custom_exceptions import *

class Item:            
    def __init__(self, name, quantity):
        self.set_name(name)
        self.set_quantity(quantity)
        self.locked = False
        
    def __str__(self):
        return self.name

    def set_name(self, name):
        if(type(name)is not str):
            raise ValueError("Name must be a string")
        else:
            self.name = name
           
    def set_quantity(self, quantity):
        if(type(quantity) is not int or quantity < 0):
            raise ValueError("Quantity must be a positive integer")
        else:
            self.quantity = quantity
    
    def take_item(self):
        if (self. quantity > 0):
            self.quantity -= 1
        else:
            raise OutOfStock
        
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
        if (self.item_exists(item)):
            self.items[item].locked = True
        else:
            raise InvalidItemType()
    
    def unlock(self, item):
        if (self.item_exists(item)):
            self.items[item].locked = False

    def validate_purchase(self, item):
        if (not self.item_exists(item)):
            raise InvalidItemType
        elif item.locked == False:
            raise ItemNotLocked
        elif self.items[item].quantity <= 0:
            raise OutOfStock
        else:
            self.items[item].take_item()
        return self.items[item].quantity
    
    def buy_item(self, item):
        try:
            self.lock(item)
            num_left = self.validate_purchase(item)
        except InvalidItemType:
            print("Sorry, we don't sell {}".format(str(item)))
        except OutOfStock:
            print("Sorry, the item is out of stock.")
        else:
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