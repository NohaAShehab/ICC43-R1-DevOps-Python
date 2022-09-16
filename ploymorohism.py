"""

    ploymorphism ---> many faces

    ---> overloading
        --> 2 functions with the same name in the same class but different in the arguments (type, no.)
        ==? dispatch (implict)
    --> overriding
        -===> 2 functions (one in the parent class) --> the other in the child class with the same name
        and the same arguments but different in the implementation

"""

class Employee:
    def __init__(self,name=''):
        self.name= name

    def speak(self, message = ""):
        print(f"My name is {self.name}, {message}")

# e =Employee("Ahmed")
# e.speak()

class Teacher(Employee):
    def __init__(self,name,email='iti@iti.com'):
        super().__init__(name=name)
        self.email = email

    # override
    def speak(self, message = ""):
        super().speak(message=message)
        print("I am a teacher ")

t= Teacher("noha")
t.speak("testtt message ")