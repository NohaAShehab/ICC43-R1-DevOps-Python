"tuple like list ---> is immutable "

"1- to define a list"
t = ()
myt = tuple([])


"2- tuple can hold different values from different datatypes"
courses = ("python", "devops", True, 14, 2022,  "python",
           ["ansible", "docker", "kubernetes"],
           "python")

"3- can access its elements using index --> start from zero"
print(courses[2])
print(courses[6][2])
courses[6].append(10)
print(courses[6], type(courses[6]))
courses[6][2]="update"
# courses[2]= "updated"  # invalid

"4- get len of the tuple"
print(len(courses))

"5 - check if the items exists or not "
if 'python' in courses:
    print('found')

"6- loop over the tuple"
for i in courses:
    print(i)

"7- concat tuples "
t1= ("kubernate", "ansible")
t2 = ('GCP', "docker")
concatetuple = t1 + t2

# l = ["ahmed", "ali",  "yossef", "noha", "mohmed"]
# # l.sort()
# print(l)
# print(l.sort())
# print(l)
# courses.sort()
# "8- count element in l"
#
# print(courses.count("python"))
#
# "8- get index of the element "
# print(courses.index("python"))

########### convert list to tuple and vice versa


l = ["ahmed", "ali", "yossef", "noha", "mohmed"]

myt= tuple(l)
# print(l, type(l))

newlist = list(myt)
print(newlist, type(newlist))
