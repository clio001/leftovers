import sqlite3
from item import Item


class Database:
    DATABASE_LOCATION = './haushalt.db'  # this is a constant for things like paths
    item = ''

    def __init__(self):
        return

    def create_database(self):
        connect = self.get_database_connection()  # dont repeat yourself -> move to a method

        connect.close()

    def add_item_to_database(self, item: Item):
        connection = self.get_database_connection()  # dont repeat yourself -> move to a method

        # the ? stands for one attribut
        # the 2 (!) attributes come from the item itself now
        # before you injected an item here !?
        connection.execute('insert into tiefkuehler values(?,?,"heute")', (
            item.get_name(),
            item.get_amount()
        ))

        connection.commit()

        self.close_database_connection(connection)  # dont repeat yourself -> move to a method

    def update_item_from_database(self):
        return

    def delete_item_from_database(self):
        return

    # printing out is kind of misplaced here though...
    # method says "get_something" not "get_and_print_something"
    def get_content_from_database(self):
        connection = self.get_database_connection()  # dont repeat yourself -> move to a method
        cursor = connection.execute('select * from tiefkuehler order by Essen asc;')

        for row in cursor:
            print(str(row[2]) + ', ' + str(row[1]) + ', ' + str(row[0]))

        print('\n')  # nice to look at

        self.close_database_connection(connection)

    def get_database_connection(self):
        return sqlite3.connect(self.DATABASE_LOCATION)

    def close_database_connection(self, connection):
        connection.close()
