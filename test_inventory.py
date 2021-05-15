from item_inventory import *

# Create instances of Item
iphones = Item("iPhone", 2)
samsung_phones = Item("Samsung", 11)
item1 = Item("item1", 2)

# Create an instance of Inventory
online_store = Inventory()
# Add item stacks in Inventory
online_store.add_item(iphones)
online_store.add_item(samsung_phones)

# Test the Inventory instance
online_store.buy_item(iphones)
online_store.buy_item(iphones)
online_store.buy_item(samsung_phones)
online_store.buy_item("jfdkdsk")
online_store.buy_item(item1)