"""
    to write data in the file

    fileobject =open(filename, "a")
    ---> mode "a" ---> append mode--> each time you open the file with it
     ---> open the file for writing starting from the end of the file
    ---> file exists  --> keep its content ===>
    ---> file not exists? --- > try to create it
"""
try:
    fileobj= open("mycv.txt", "a")
except Exception as e:
    print(e)
else:
    fileobj.write("new line addedd  \n")
    fileobj.write("-------------------------- \n")
    fileobj.close()