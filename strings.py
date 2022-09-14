
"-------------------------strings----------------"

# username= 'Ahmed'  # string is treated like an array --> each char has index start from 0
# "1- get the length of the string"
# print(len(username))
# "2- access chars of the string using index "
# print(username[2])
# print(username[2:4])  # chars at index from start to end-1
# print(username[-1]) # d
#
# "3- concatenation"
# h = "Hello "
# w = "World"
# hw = h + w
# print(hw)
#
# "4- interpolation"
# fname = 'Noha '
# mid = "AbdelHady "
# lname = "Shehab"
# # fullname = fname + mid + mid + lname
# fullname = fname + mid*2 + lname
# print(fullname)
#
# "5- replace part of the string "
# print(fullname.replace("a", "@"))
#
# "6- count no of chars in the string"
# print(fullname.count("a"))
#
# "7- get the index of char in the string"
# print(fullname.index("a"))  # get the index of the first occurrence of the string
#
# "8- check the content of the string"
# " check if the value in the string is numeric"
# year = "2022"  #string varaible ---> value in it is digit 0--->9
# print(year.isdigit())  #
# print(type(year))
#
# " check if the value in the string is alpha a-z"
# name = 'noha '
# print(name.isalpha())
#
# "check if the value is spaces "
# info = "                                     "
# print(info.isspace())
#
# "check if the value in the string ---> in upper case or lower ---> Check all the chars"
# name = "AHMED"
# print(name.isupper()) #
# print(name.islower())
#
# "9- Captilize the chars"
# msg = 'i love python.'
# print(msg.capitalize())
# print(msg.upper())
# print(msg.lower())
#
# "10- format string "
# # temp = "my name is {0}, I works at {1}"
# # print(temp.format("noha", "iti"))
# # print(temp.format("Ahmed", "VOIS"))
# # print(temp.format("Valeo", "Ali"))
# temp = "my name is {username}, I works at {company}"
# print(temp.format(company='Valeo',username='Ali'))
#
# "11- f format string .... "
# firstname = input("please enter firstname ...: ")  # input read input from user and put it into string
# lastname = input("please enter last name ... ")
# day = 14
# msg = f"Greeting Mr {firstname} {lastname}, nice to meet you, {day} "
# print(msg)
import string

"operation on the result of input"
# sal = input("please enter your salary ,,, : ")
# print(type(sal))
# if sal.isdigit():
#     sal = int(sal)
#     print(type(sal), sal)

# sal = int(input("please enter sal ,,, "))
# print(sal)

### loop over the string
# for i in list(string.ascii_lowercase):
#     print(i)
#
# print("----------------")

"11- strip the string ............... "

# greeting = '          My name is Noha , Nice to meet you all                '
# print(len(greeting), greeting)
# m = greeting.strip()  # remove the space from the beginning and the end of the string only
# print(len(m), m)

# message = "       Nice to meet you $         "
# print(message.rstrip("$ ueciNc"))  # remove set of the char from the string edges
#
# print(round(5.66))
# print(min(55,66,77,88))
# print(sum([5,6,6]))
#
# # ############ bool
# t = True
# f = False
#
# x = 10 and True












