"""
    limit accessibility of class items ---> functions , variables
    -----------------Access modifiers ---------------------
    public -=====> can be accessed using instance
    protected  --->can be accessed only in the class or the derived class
    private ---> can be accessed only in the class
    static --> accessed with classname ==== Class variable , class method

    --- in python no access modifiers


"""

# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email= email  # protected_property
#         self.__salary= salary # private_property
#         # this variable is private and can be accessed only in the class
#
#
# e = Employee("noha", 'noha@gmail.com', 1000)
# print(e.name)
# e.name = 'Noha Shehab'
# print(e._email) # itworks but don't do that
# print(e.__salary)

####################################3


# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email= email  # protected_property
#         self.__salary= salary # private_property
#
#     ## setter , getter
#     def setSalary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int):
#             self.__salary = sal
#         else:
#             self.__salary = 0
#
#     def getSalary(self):
#         return self.__salary
#
# e = Employee("noha", 'noha@gmail.com', 1000)
# print(e.name)
# e.name = 'Noha Shehab'
# print(e._email) # itworks but don't do that
# print(e.getSalary())
# e.setSalary("iti")

####################################


# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email= email  # protected_property
#         self.__salary= salary # private_property
#         self.__test()
#
#     def __test(self):
#         print("test function")
#
#     ## setter , getter
#     def setSalary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int):
#             self.__salary = sal
#         else:
#             self.__salary = 0
#
#     def getSalary(self):
#         return self.__salary
#
# e = Employee("noha", 'noha@gmail.com', 1000)
# print(e.name)
# e.name = 'Noha Shehab'
# print(e._email) # itworks but don't do that
# print(e.getSalary())
# e.setSalary("iti")
# # e.__test()

#################################33
# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name  # public
#         self._email= email  # protected_property
#         self.__salary= salary # private_property
#     # calculated field
#     @property
#     def netSal(self):
#         return self.__salary*.86
#
#     ## setter , getter
#     def setSalary(self, sal):
#         if isinstance(sal, float) or isinstance(sal, int):
#             self.__salary = sal
#         else:
#             self.__salary = 0
#
#     def getSalary(self):
#         return self.__salary
#
# e = Employee("noha", 'noha@gmail.com', 1000)
# print(e.netSal)
# # e.__test()

#######################################################3

class Employee:
    def __init__(self,name, email, salary):
        self.name = name  # public
        self._email= email  # protected_property
        # self.__salary= salary # private_property
        self.salary = salary
    # calculated field
    @property
    def netSal(self):
        return self.__salary*.86

    @property
    def salary(self):
        # self.__salary += 10
        return self.__salary

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, float) or isinstance(sal, int):
            self.__salary = sal
        else:
            self.__salary = 0


    ## setter , getter
    # def setSalary(self, sal):
    #     if isinstance(sal, float) or isinstance(sal, int):
    #         self.__salary = sal
    #     else:
    #         self.__salary = 0

    # def getSalary(self):
    #     self.__salary +=10
    #     return self.__salary


# e = Employee("noha", 'noha@gmail.com', 1000)
# print(e.netSal)
# print(e.salary)  # property
# e.salary = "iti" # property

e= Employee("noha", 'n@mgail.com', 'iti')  #__init__
e.salary = "iti"

print(e.__dict__)


















