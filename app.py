from item import Item
from database import Database


MyFreezer = Database()

food = 'fish'
amount = '1'

item_object = Item(food, amount)  # no setter needed if setting is happening in __init__ method

print("\nThe item is: ", item_object.get_name(), item_object.get_amount(), '\n')

MyFreezer.create_database()

print('The freezer contained following items')
print(50 * '=')
MyFreezer.get_content_from_database()

MyFreezer.add_item_to_database(item_object)

print('The freezer contained following items')
print(50 * '=')
MyFreezer.get_content_from_database()
