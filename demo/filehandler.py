

def save_new_book(bookdetails):
    try:
        fileobj=open("books.txt", "a")
    except:
        print("----- issue while creating the book ")
        return False
    else:
        fileobj.write(f"{bookdetails}\n")
        return True



def get_books_from_file():
    try:
        fileobj = open("books.txt")
    except Exception as e:
        print("---- error happened while openeing the file .. try again ")
        return False
    else:
        books = fileobj.readlines()
        fileobj.close()
        return books


def search_book_by_id(book_id):
    allbooks = get_books_from_file()
    for book in allbooks:
        # print(book)
        mybook = book.strip("\n")
        mybook = mybook.split(":")
        if mybook[0]==str(book_id):
            book_index = allbooks.index(book)
            print(f"book found at index {book_index} , ")
            return True, book_index
    else:
        print("book not found ")
        return False


def write_book_list_to_the_file(booklist):
    try:
        fileobj = open("books.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(booklist)
        fileobj.close()
        return True

def delete_Book_from_file(book_id):
    book_found = search_book_by_id(book_id)
    print(book_found)
    if book_found:
        print("boook founddddddddddddddddd")
        book_index = book_found[1]
        allbooks = get_books_from_file()
        del allbooks[book_index]
        # print(allbooks)
        ### delete book from the list ---->
        # write the book list again to the file
        deleted=write_book_list_to_the_file(allbooks)
        return deleted



def edit_book_in_file(book_index, new_data):
    allbooks = get_books_from_file()
    allbooks[book_index]= f"{new_data}\n"
    edited=write_book_list_to_the_file(allbooks)
    if edited:
        print("---- book updated successfully---- ")
