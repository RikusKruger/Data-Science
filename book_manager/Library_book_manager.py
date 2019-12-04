import sqlite3


class Bookstore:

    def __init__(self, data, cursor):
        self.database = data
        self.cursor = cursor

    def createtable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books(ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, 
                            Qty INTEGER)''')

    def insert(self, ID, title, author, qty):
        try:
            self.cursor.execute('''INSERT INTO books(ID, Title, Author, Qty)
                                VALUES(?, ?, ?, ?)''', (ID, title, author, qty))
            self.database.commit()
        except Exception as e:
            print(e)
            return

    def update(self, field, field_value, condition, condition_value):
        update = f"UPDATE books SET {field}={field_value} WHERE {condition}={condition_value}"
        self.cursor.execute(update)
        self.database.commit()

    def delete(self, condition, condition_value):
        delete = f"DELETE FROM books WHERE {condition}={condition_value}"
        self.cursor.execute(delete)
        self.database.commit()

    def find(self, condition, condition_value):
        select = f"SELECT ID, Title, Author, Qty FROM books WHERE {condition} = {condition_value}"
        self.cursor.execute(select)
        found = self.cursor.fetchone()
        print(found)

if __name__ == '__main__':
    data = sqlite3.connect('ebookstore.db')
    cursor = data.cursor()
    bookstore = Bookstore(data, cursor)
    bookstore.createtable()
    try:
        bookstore.insert(3001, 'A Tale of Two Cities', 'Charles Dickens', 30)
        bookstore.insert(3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40)
        bookstore.insert(3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25)
        bookstore.insert(3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)
        bookstore.insert(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
        bookstore.database.commit()
    except Exception as e:
        print(e)

    while True:
        menu = int(input("Book Manager\n\n Please select a option:\n1. Enter book\n2. Update book\n3. Delete book\n4. Search books\n0. Exit\n\n"))

        if menu == 1:
            print("NEW BOOK")
            ID = input("Please enter book ID: ")
            title = input("Please enter book title: ")
            author = input("Please enter book author: ")
            qty = input("Please enter book qty: ")
            bookstore.insert(ID, title, author, qty)
            bookstore.database.commit()

        elif menu == 2:
            print("UPDATE BOOK")
            field = input("Please enter the field you wish to update(ID, Title, Author, Qty): ")
            field_value = input("Please enter the value for said field: ")
            condition = input("Please select how to identify book(ID, Title): ")
            condition_value = input("Please enter the identifier value: ")
            bookstore.update(field, field_value, condition, condition_value)
            bookstore.database.commit()

        elif menu == 3:
            print("DELETE BOOK")
            condition = input("Please select how to identify book(ID, Title): ")
            condition_value = input("Please enter the identifier value: ")
            bookstore.delete(condition, condition_value)
            bookstore.database.commit()

        elif menu == 4:
            print("FIND BOOK")
            condition = input("Please select how to identify book(ID, Title, Author, Qty): ")
            condition_value = input("Please enter the identifier value: ")
            bookstore.find(condition, condition_value)

        elif menu == 0:
            exit()
