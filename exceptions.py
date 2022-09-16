


# def sumnum(x,y):
#     return x*y
#
#
# ## write test cases for your application
#
#
# print("hello world")
##########################################################################
":exceptions"
# print("------ Exceptions --------------")
# print(name)
#
# print("----------------------------------")

"""  when the exception detected , the module execution will stop ----"""
###########################################################
""" databases , network , files, casting ---"""
# print("======= before exception ===============")
# try:
#     print(coursename)
# except:
#     print("-------- issue with the variable ------")
#
#
# print("------- execution completed successfully ------- ")

##########################################################

# print("======= before exception ===============")
# try:
#     # print(coursename)
#     print(6/0)
# except Exception as e :
#     print(f"-------- issue with : {e} ------")
#
#
# print("------- execution completed successfully ------- ")


#################### action depends on this code

# print("======= before exception ===============")
# try:
#     # print(coursename)
#     x = 6/0
# except Exception as e :
#     print(f"-------- issue with : {e} ------")
#     x = 0
# else:
#     "this block will be executed when there is no problem "
#     x += 5
#
#
# print(x)

print("------- execution completed successfully ------- ")

#################################################
# def divnums():
#     num1 = input("please enter num1 ")
#     num2 = input("please enter num2 ")
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#     except:
#         print("------ you should enter num1 , num2 to be numbers")
#         return divnums()
#     else:
#         if num2==0:
#             print("division by zero is not allowed ")
#             return divnums()
#         res = num1/ num2
#         print(res)
#         return res   ###3 exce
# #
# res= divnums()
# print(res)
############################ finally
# print("======= before exception ===============")
# try:
#     # print(coursename)
#     # x = 6/0
#     print(m)
# except ZeroDivisionError as e :
#     print(f"-------- issue with : {e.args} ------")
#     print(type(e.args[0]))
#     x = 0
# except NameError as n:
#     print(f"-------- issue with____ : {n} ------")
#     m = None
# except Exception as e:
#     print(f"----- {e}------")
# else:
#     "this block will be executed when there is no problem "
#     x += 5
#     print(x)
# finally:
#     "this block will be executed if there is problem or not ...."
#     print("------------end of the process")

########################################################################################################3
############################## Raise Exception #########################
def askfornum(message):
    num = input(message)
    try:
        num = float(num)
    except:
        print("---- please enter valid number ----")
        return askfornum(message)
    else:
        return num

def divnums():
    num1 = askfornum("please enter num1: ")
    num2 = askfornum("please enter num2: ")
    if num2==0.0:
        raise Exception("we cannot divide by zero ")

    print(f"num1= {num1}, num2= {num2}")

    res = num1/ num2
    return res
try:
    dividedd = divnums()
except Exception as e:
    print(f"{e}")
    dividedd = divnums()


































