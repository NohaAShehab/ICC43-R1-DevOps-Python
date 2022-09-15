"""  functions with know number of arguments -----------------------"""
# def getfullname(firstname, lastname):  #2
#     pass


# def getfullname(firstname, lastname):  # arguments
#     fullname = f'{firstname} {lastname}'
#     print(fullname)
#     return
#
#
# x = getfullname("Noha", "Shehab")
# print(x)  # None object

###################################
# def getfullname(firstname, lastname):  # arguments
#     fullname = f'{firstname} {lastname}'
#     print(f"---- in the function ---- {fullname}")
#     return fullname

# x = getfullname("Noha", "Shehab")
# print(x)  # None object

# def helloworld():
#     print("Hello world")
#
# helloworld()


# ############################### function default argument
# def sumnum(num1=9, num2=0):  # arguments   #from zero to 2 ?
#     print(f"num1 = {num1}, num2={num2}")
#     return num1 + num2
#
# z = sumnum(10,20)
# m = sumnum(10)
# mm = sumnum()


# ################################### take a breath
# def sumnum(num1, num2):
#     return num1 + num2
#
#
# res = sumnum(10,10)
# print(res)
#
# res = sumnum("10","10")
# print(res)
#
#
# res = sumnum("10",9)
# print(res)
###########################
def sumnum(num1: int, num2: int):  # for Your information
    # # make sure the value --->
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
# sumnum(2,4,5)
#     print("you should enter valid numbers ")
#
#
# res = sumnum(10,10)
# print(res)
# print('----------------------------------')
# res = sumnum("10","10")
# print(res)
# print('----------------------------------')
# #
# res = sumnum("10","iii")
# print(res)

#########################################
""" function accept unknown number of arguments ---- """

#
# def sumnummm(*args):  # function accept zero or more argument
#     print(args, type(args))  # tuple
#     res = 0
#     for item in args:
#         res +=item
#     print(f"------------sum = {res} ------------------")
#
# sumnummm()
# sumnummm(19,20)
# sumnummm(4,6,7,8,9)
# sumnummm(55,666)
#
# # print(max(3,5,6,666))
# #
# # print(max(19,22, 888888, 88888888))
# #
# # print("noha", "Mona","ahmed")

"""   """


# def introduceYourSelf(** kwargs):
#     print(kwargs)  # dictionary
#     print("------------------------------")
#
#
# introduceYourSelf(name='noha', works='iti')
# introduceYourSelf()
# introduceYourSelf(fname='noha', lname='shehab', city='cairo')
# introduceYourSelf(lastname='', age= 25)
###########################333



def test(*args, **kwargs):
    print(args)
    print(kwargs)
    print('-----------------------------')


test()
test(10)
test(name='ahmed', track='devops')
test('iti', name='ali')
