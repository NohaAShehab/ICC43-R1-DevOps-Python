import  time
from filehandler import save_new_book, get_books_from_file, delete_Book_from_file, \
    search_book_by_id, edit_book_in_file
def askfornum(message):
    num = input(message)
    try:
        num = int(num)
    except:
        print("---- please provide number not a string ---- ")
        return askfornum(message)
    else:
        return num

def askforstr(message):
    mystr = input(message)
    if mystr.isspace() or not mystr:
        print("---- please provide suitable string ")
        return askforstr(message)
    return mystr

def askfordetails():
    title= askforstr("please enter the title: ")
    author= askforstr("please enter the author name: ")
    no_of_pages = askfornum("please number of pages: ")
    return title, author, str(no_of_pages)


def generate_new_id():
    id = round(time.time())
    return id

def createBook():
    print("---- create book ---- ") ## ask user about the book details
    details = list(askfordetails()) # for each new book ----> generate _id
    id = generate_new_id() #### prepare the data
    details.insert(0, str(id)) ### merge the book details into one line
    "join ---> join the list elements into one string using seperator "
    book_details = ":".join(details)
    ## save it in the file
    added = save_new_book(book_details)
    if added:
        print("---- new book added successfully ")
    else:
        print("---- error happened , try again now ")
        return createBook()


def listallBooks():
    # get the data from the file
    books = get_books_from_file()
    if books==False:
        print('-----------no available books ------ ')
    else:
        print(books)



def deleteBook():
    print("------------ list of the avaiable books ------------------- ")
    listallBooks()
    book_id = askfornum("please choose id of the book you want to delete: ")
    # print(book_id)
    deleted=delete_Book_from_file(book_id)
    if deleted:
        print("---- book deleted successfully ---- ")


def editBook():
    print("------------ list of the avaiable books ------------------- ")
    listallBooks()
    book_id = askfornum("please choose id of the book you want to edit: ")
    book_found = search_book_by_id(book_id)
    print(book_found)
    if book_found:
        newDetails=list(askfordetails())
        print(newDetails)
        ## repalace old_data with data
        newDetails.insert(0, str(book_id))
        newbook_details = ":".join(newDetails)
        print(newbook_details)
        edit_book_in_file(book_found[1],newbook_details)

