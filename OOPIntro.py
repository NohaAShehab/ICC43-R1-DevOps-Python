"""
    object contains data as well as functionality
    --> create structure


"""
# emp1= {
#     "name":"Ahmed",
#     "company": "VOIS",
#     "salary": 20000
# }
#
# emp2= {
#     "firstname":"Ahmed",
#     "companyname": "VOIS",
#     "salary": 20000
# }

""" create my own datatype  ---> using classes 
    OOP ---> keywords
        class ---> blueprint for a type ---> define properties , methods 0->that object have/ can do
    
    OOP --> principle
"""

# l = []
# print(type(l))

# class Employee:
#     pass
#
#
# "1- take object from Employee"
# e = Employee()
# print(type(e))
# print(e)  # object address
# e.name = 'Ahmed'
# e.salary = 20000
#
#
# e2 = Employee()
# e2.firstname='Mohamed '


########################################################################3
""" control object creation 000> determine parameters in the object"""

# class Employee:
#     def __init__(self):  # constructor function ---> calling while the object
#         print(self)  # self  ---> address of the object in the memory
#         print("---- this function is called while creating the object ----- ")
#         self.name = "Ahmed"
#         self.salary = 20000
#
# e = Employee()
# print(e)
#
# e3 = Employee()
"""
    box (iphone, connector)
    iphone14 = box (iphone, connector)
    iphone8 = box(iphone, charger, connector, headphones)
    iphone13=  box (iphone, connector)
"""
#
# class Employee:
#
#     def __init__(self, n, sal):  # constructor function ---> calling while the object
#         print(self)  # self  ---> address of the object in the memory
#         print("---- this function is called while creating the object ----- ")
#         # name , salary are instance variables --->their values depend on the instance
#         self.name = n
#         self.salary = sal
#
#
# e = Employee("Ahmed", 20000) #
# print(e)
# e.email = 'ahmed@gmail.com' # email will be added to the e instance only....
# e3 = Employee("Ali", 30000)
###########################3

""" prevent modifying object structure """

# class Employee:
#     __slots__ = ["name", "salary"]
#     def __init__(self, n, sal):  # constructor function ---> calling while the object
#         print(self)  # self  ---> address of the object in the memory
#         print("---- this function is called while creating the object ----- ")
#         # name , salary are instance variables --->their values depend on the instance
#         self.name = n
#         self.salary = sal
#
#
# e = Employee("Ahmed", 20000)  #
# print(e)
# e.email = 'ahmed@gmail.com'  # email will be added to the e instance only....
# e3 = Employee("Ali", 30000)

##################################################################################
"""   instance  ==== object       
    self ---> reference in the object 
    __init__ ---> constructor   
"""

# class Employee:
#     def __init__(self, n, sal):
#         self.name = n  # instance variable
#         self.salary = sal
#
#     # # instance method ---> define behaviour that object can do---> behaviour depends on instance, object
#     def speak(self):
#         # "self is the object"
#         print(f"My name is {self.name}")
#
#
# e = Employee('noha', 1000)
# print(e.__dict__)  # represent the object in a dictionary
# e.speak()
#######################################################################
""" property ---> represent the class ===> shared between all instances """

#
# class Employee:
#     nationality = 'Egyptian'  # ## class variable
#     # this property is shared between all the instances
#     ## value of this property depends on the class not on the instance
#     def __init__(self, n, sal):
#         self.name = n
#         self.salary = sal
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# e = Employee("Ahmed", 20000)
# e2 = Employee("Ali", 40000)
# # you can access it using class name
# print(Employee.nationality)
# Employee.nationality = "American"

######################################## modify the class variable via instnace
#
# class Employee:
#     nationality = 'Egyptian'  # ## class variable
#     no_of_emps= 0
#     def __init__(self, n, sal):
#         self.name = n
#         self.salary = sal
#         Employee.no_of_emps +=1
#         self.id= Employee.no_of_emps
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# e = Employee("Ahmed", 20000)
# e2 = Employee("Ali", 40000)
# # you can access it using class name
# print(Employee.nationality)
# # e.nationality = "American"  # add new instance variable to the object with the same name nationality
#
# ######################### class method
#
# class Employee:
#     nationality = 'Egyptian'  # ## class variable
#     no_of_emps = 0
#
#     def __init__(self, n=None, sal=None):
#         self.name = n
#         self.salary = sal
#         Employee.no_of_emps += 1
#         self.id = Employee.no_of_emps
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#     # class method ---> behaviour depend on the class not the instance
#     @classmethod  # built-in decorator
#     def get_no_of_employees(cls):  # cls ---> represent the current class
#         print(cls)
#         return cls.no_of_emps
#
#     ### class method ---> used as object factory
#     @classmethod
#     def create_default_object(cls):
#         return cls(None,None)
#
#     @classmethod
#     def add_employees(cls, emp1, emp2):
#         if isinstance(emp1, cls) and isinstance(emp2, cls):
#             return cls(f"{emp1.name}{emp2.name}", emp1.salary+emp2.salary)
#
#
# e = Employee("Ahmed", 20000)
# e2 = Employee("Ali", 40000)
# print(Employee.get_no_of_employees())
# print(Employee.no_of_emps)
# e3= Employee.create_default_object()
#
# e4 = Employee.add_employees(e,e2)
# print(e4.__dict__)
#################################################
""" static methods """


class Employee:
    nationality = 'Egyptian'  # ## class variable
    no_of_emps = 0

    def __init__(self, n=None, sal=None):
        self.name = n
        self.salary = sal
        Employee.no_of_emps += 1
        self.id = Employee.no_of_emps

      # used as a helper method -->
    @staticmethod
    def calnetSal(sal):
        print(sal)
        # return sal * .86



e = Employee("Ahmed", 30000)
print(Employee.calnetSal(e.salary))
print("------------------------")
print(Employee.calnetSal(50000))
# print(e.calnetSal())
# def calnetSal(sal):
#     return sal * .86
#
#
# netsal = calnetSal(e.salary)
# print(netsal)

# print(calnetSal(40000))
