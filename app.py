from item import Item
from database import Database

item_object = Item()

MyFreezer = Database()

food = 'fish'
amount = '1'

item = (food, amount)

item_object.create_item(item)

print("The item is: ")
item_object.display_item()

MyFreezer.create_database()

MyFreezer.get_content_from_database()

MyFreezer.add_item_to_database(MyFreezer.item)