"""

    define where the variable will be accessed

    lexical scope --->
"""

""" 1- Global scope ---
        any variable defined in the python script ---> its scope --> Global scope ===>
        variable can be read any where in the script 
        you can modify the value of the global varaible from inside the function using
        global variablename
        
        
    2- variable with localscope : 
        any variable defined in the function can be accessed only inside the function
"""


#
# name = 'Ahmed'  # varaible is defined in the global scope ,,,
#
#
#
# def checkname():
#     print(f"calling the check name function ----> name = {name}")
#
# print(name)
# checkname()
#############################################################################3
# """ modify the global variable from outside the function """
#
# name = 'Ahmed'  # varaible is defined in the global scope ,,,
#
#
# def checkname():
#     print(f"calling the check name function ----> name = {name}")
#
#
# name = 'Ali'
# print(name)
# checkname()
###################################################
""" modify the global variable from the function """
#
# # name = 'Ahmed'  # varaible is defined in the global scope ,,,
# # def checkname():
# #     name = 'Ali' # create new local variable for the function
# #     print(f"calling the check name function ----> name = {name}")
# #
# # checkname()
# # print(name)
#
# name = 'Ahmed'  # varaible is defined in the global scope ,,,
# def checkname():
#     # global name
#     name = 'Ali' # create new local variable for the function
#     print(f"calling the check name function ----> name = {name}")
#
# checkname()
# print(name)
# print("-------------------------------")







# ###########################################

""" Python support functional programming, OOP """


""" you can define function inside a function
    local variable of the function can be accessed only inside the function 
"""

# def outerfunction():
#     course = 'python'  # course is local variable for the outerfunction
#     print(f"outer ----> {course}")
#     def sayhello():  # localfunction iside the outerfunction , cannot accessed outside the outerfunction
#         print(f" from the function ----> {course}")
#         print("---------------------------------")
#     sayhello()  # this function is called in the outer function scope
#     print(f" ####################---> {course}")
#
#
# outerfunction()




# def outerfunction():
#     course = 'python'  # course is local variable for the outerfunction
#     print(f"outer ----> {course}")
#     def sayhello():  # localfunction iside the outerfunction , cannot accessed outside the outerfunction
#         course= 'django'  # new local variable for the function sayhello
#         print(f" from the function ----> {course}")
#
#     sayhello()  # this function is called in the outer function scope
#     print(f" ####################---> {course}")


#################################################33
#
# track = 'opensource '
#
# def outerfunction():
#     course = 'python'  # course is local variable for the outerfunction
#     print(f"outer ----> {course}")
#     def sayhello():
#         nonlocal course
#         course= 'django'  # new local variable for the function sayhello
#         global  track
#         track = 'devops'
#         print(f" from the function ----> {course}")
#
#     sayhello()  # this function is called in the outer function scope
#     print(f" ####################---> {course}")
#
# print(track)
# outerfunction()
# print(track)

####################################33
track = 'test'

def A():
    global track
    track = 'opensource'
    def B():

        def C():
            nonlocal track
            track = "devops"

        C()
    B()

    print(track)

A()
































