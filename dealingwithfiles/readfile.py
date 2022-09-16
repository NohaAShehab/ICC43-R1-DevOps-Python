"""
    python ---> read from a file ---->
    open ("filename/filepath", mode )
    mode ---> open the file for ? read , write , execute

    -------------- to deal with file -------
    1- open file
        fileobject=open(filename, mode) ----> mode r ---> read , w---> write, a ---> append
        fileobject ---> type TextIOWrapper  ---> filename , mode ---> encoding
    2- do the operation (read , write)
        fileobject.read()
        fileobject.write()
    3- close the file
        fileobject.close()
"""
try:
    # fileobj=open("students.txt", "r")
    fileobj = open("students.txt") # open the file for reading
except Exception as e:
    print(e)
else:
    print(fileobj)
    # "read file content into one string"
    # data = fileobj.read()  # read the file content into one string
    # print(data, type(data))
    "read the file line by line "
    # l = fileobj.readline()
    # print(l, type(l))
    "read file lines into a list"
    lines = fileobj.readlines()
    print(lines)
    fileobj.close()






