"""

    console application for library


    add , edit , delete , display information of the books

    create:
        title , no_of_pages, author_name

"""
from bookoperations import createBook, listallBooks, deleteBook, editBook


def mainmenu():
    choice= input("please enter n for new book , l for listing all books, e for edit, d for delete ")
    if choice =="l":
        print("---- list all books -----")
        listallBooks()
    elif choice =="n":
        createBook()
    elif choice =="e":
        editBook()
    elif choice =="d":
        deleteBook()
    else:
        print("---- no correct choice ----")
        return mainmenu()

mainmenu()