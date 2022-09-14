"""
lists are non primitive datatype

mutable --> change its content in the runtime
"""
"1- to define a list"
l = []
myl = list([])

"2- list can hold different values from different datatypes"
courses = ["python", "devops", True, 14, 2022,  "python",["ansible", "docker", "kubernetes"], "python"]

"3- can access its elements using index --> start from zero"
print(courses[2])
print(courses[5][2])
courses[2]= "updated"
# courses[10]= "added"  # list assignment index out of range
"4- get len of the list"
print(len(courses))
if len(courses)> 10:
    courses[10] = "added"

"5- append element to the list --> add the end of the list"
courses.append("new element")

"6- insert element at certain index in the list"
courses.insert(2, "inserted")

"7- pop element form the list "
popped = courses.pop() # pop the last element in the list and return with it
print(popped)
"8- pop element at certain index "
newpopped = courses.pop(3)

"9- remove certain item --> remove the first of occurrence of the element"
courses.remove('python')

"10 - check if the items exists or not "
# if 'python' in courses:
#     courses.remove('python')

"11- loop over the list"
# for i in courses:
#     # print(i)
#     if i == 'python':
#         courses.remove(i)

"12 concat lists "
l1= ["kubernate", "ansible"]
l2 = ['GCP', "docker"]
courselist = l1 + l2


'13- extend list'

l1= ["kubernate", "ansible"]
l2 = ['GCP', "docker"]
l1.extend(l2)


"14-  sort the list ---> sort the lists --> elements have the same type "
"sort the same object"
# # l =[50000000,766,7,8888,199]
# # print(l.sort())
# l = ["h","ali", "Ahmed"]
# print(l.sort(reverse=True))

"15- reverse the list"
myl = ["test", 19, True, "Ahmed", "Python"]
myl.reverse()
print(myl)
""" difference between sort , sorted ....."""

"16- count element in l"

print(courses.count("python"))

"17- get index of the element "
print(courses.index("python"))
