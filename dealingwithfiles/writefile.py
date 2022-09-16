"""
    to write data in the file

    fileobject =open(filename, "w")
    ---> mode "w" ---> write mode--> each time you open the file with it
     ---> open the file for writing starting from the beginning of the file
    ---> file exists  --> remove its content ===>
    ---> file not exists? --- > try to create it
"""
# try:
#     fileobj = open("mycv.txt", "w")
# except Exception as e :
#     print(e)
# else:
#     print(fileobj)
#     fileobj.write("Noha Shehab\n")
#     fileobj.write("ITI\n")
#     fileobj.write("---------------------------\n")
#     fileobj.writelines(["line1\n", "Line2\n", "Line3\n"])
#     fileobj.close()
#     # fileobj.write("Noha Shehab\n")



###################################


with open("mycv.txt", "w") as fileobject:
    fileobject.write("bla bla bla ")  # return number of written bytes
    




