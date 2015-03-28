__author__ = 'Davidjohn Blodgett'


class Library:
    # Attributes
    __Shelves = []

    # Constructor
    def __init__(self):
        print("A Library created!")

    # Object Methods
    def add_shelf(self, Shelf):
        self.__Shelves.append(Shelf)

    def remove_shelf(self, Shelf):
        self.__Shelves.remove(Shelf)

    def list_books(self):
        if len(self.__Shelves) <= 0:
                print("No Shelves found!")
        else:
            for x in self.__Shelves:
                print("Shelf %d has the below books:" % ((x + 1)))
                self.__Shelves[x].list_books()


class Shelf:
    # Attributes
    __Books = []

    # Constructor
    def __init__(self):
        print("A Shelf has been created!")

    # Object Methods
    def add_book(self, newBook):
        self.__Books.append(newBook)
        print("%s has been placed on the shelf!" % (newBook.get_title()))

    def remove_book(self, Book):
        self.__Books.remove(Book)

    def list_books(self):
        if(len(self.__Books) <= 0):
            print("No books found!")
        else:
            for x in self.__Books:
                #a_book = self.__Books[x]
                print("Book Title is: ", x.get_title())

class Book:
    # Attributes
    __Title = None
    __Shelf = None

    # Constructor
    def __init__(self, title):
        self.__Title = title
        print("The Book, %s, has been created!" % (self.__Title) )

    # Object Methods
    def get_title(self):
        return self.__Title

    def get_shelf(self):
        if(not(self.__Shelf)):
            print("This book is not on a shelf!")
        else:
            return self.__Shelf

    def enshelf(self, Shelf):
        Shelf.add_book(self)
        self.__Shelf = Shelf

    def unshelf(self):
        self.__Shelf.remove_book(self)
        self.__Shelf = None

# Main()
if(__name__ == "__main__"):

    # create objects...
    mybook  = Book('Learn Python!!')
    myshelf = Shelf()
    mylib   = Library()

    # test what happens when nothing is in objects...
    print("\nTest when a shelf or library is empty:")
    myshelf.list_books()
    mylib.list_books()

    print("\nTest when a book is not on a shelf:")
    temp_shelf = mybook.get_shelf()
    if(not(temp_shelf)):
        print(temp_shelf)

    # test basic functionality...
    print("\nPlace", mybook.get_title(), "into the shelf!")
    mybook.enshelf(myshelf)


    print("\nAttempting to list books on shelf:")
    myshelf.list_books()


