import sqlite3
from item import Item

class Database():
    item = ''


    def __init__(self):
        return

    def create_database(self):
        connect = sqlite3.connect('/Users/john/haushalt.db')

        connect.close()


    def add_item_to_database(self, item: Item):
        connect = sqlite3.connect('/Users/john/haushalt.db')

        connect.execute('insert into tiefkuehler values(?,?,"heute")', [Item])

        connect.commit()
        connect.close()

    def update_item_from_database(self):
        return

    def delete_item_from_database(self):
        return

    def get_content_from_database(self):
        connect = sqlite3.connect('/Users/john/haushalt.db')
        print('Your freezer contains the following items:\n')

        cursor = connect.execute('select * from tiefkuehler order by Essen asc;')
        for row in cursor:
            print(str(row[2]) + ', ' + str(row[1]) + ', ' + str(row[0]))

        connect.close()