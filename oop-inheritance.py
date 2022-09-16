"""

    single multiple inheritance
    parent

    child ---> child class ---> has the properties that the parent had and can do the same functions
"""


#
# class Person:
#     def __init__(self,name):
#         self.name =name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Engineer(Person):
#     pass
#
#
# e = Engineer("Ahmed")
# e.speak()

#######################################################3


# class Person:
#     def __init__(self,name='', gender='male'):
#         self.name =name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Engineer(Person):
#     def __init__(self, name, gender, sepalization):
#         # # call parent constructor
#         super().__init__(name=name, gender= gender)
#         self.specilization = sepalization
#
#
# e = Engineer("Ahmed", "CS")
# e.speak()


#  ############################# multiple inheritance

class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, email):
        self.email = email


class C(A, B):
    def __init__(self, name, email):
        super().__init__(name=name)  # super---> constructor of the A Class ---
        # A.__init__(self, name)
        B.__init__(self, email)


obj = C("test", 'test@gmail.com')
