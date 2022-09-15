

info = ["noha","iti", "Engineering"]

""" labels  ---> dictionary --> key value pair data structure 

    key:value
    
    key ---> most cases ---> string 
    value ---> from any datatype
    
    dict ---> doesn't allow duplications in the key 


"""
"1- to define a dictionary"
# myinfo = {} # this empty dic
# mydic = dict([])

#
# myinfo = {'name':'noha', 'work':'iti'}
# mydic = dict(
#     [
#         ('name', 'Ahmed'),
#         ('track', 'devops')
#     ])
#
# "2- dict is mutable datatype --> you can access its content using the key "
# print(myinfo["name"])
# 'modify the content of element'
# mydic["name"] = 'Ali'
# 'add new key value pair to the dic'
# mydic["city"] = 'Cairo'
# print(mydic)
#
# "3- get the len of the dic "
# print(len(mydic))
#
#
# "4- doesn't allow key duplication"
# d = {"name":"Ahmed", 'track':'devops', 'name':'sabreen'}
#
#
# # m = {"ahmed", "ali", "test"}  # this is a set not a dictionary
# # print(type(m), m)
# # mydic = dict(
# #     [
# #         ('', 'Ahmed'),
# #         ( '','devops')
# #     ])
# "5- get the keys of the dic"
#
# myinfo = {'name':'noha', 'work':'iti', 'dept':'opensource'}
# keys = myinfo.keys() # special datatype dict_keys
# print(keys)  # dict_keys can be cast to a list or tuple
# # print(keys[0])
# # for k in keys:
# #     print(k)
#
# keys = list(keys)
# print(keys[0])
#
# "6- get the values of the dict"
# vals = myinfo.values()
# print(vals)  #dict_values- ---> can be casted to list or tuple
#
#
# "7- get dict element"
# elements = myinfo.items()
#
# print(elements)  # dict_items ...  can be cast to list ---> list of tuples =-->
# # each tuple has 2 values (key, value)
#
# "8- loop over the dictionary"
# # for i in myinfo:  # keys only
# #     print(f"---> {i}")
#
# for i in myinfo:  # i represent the keys only
#     print(f"---> {i} : {myinfo[i]}")
#
#
# for k,v in myinfo.items():
#     print(f"{k}:{v}")
# #
# # course = 'python'
# # student = input("please enter student name : ")
# # temp = f'Student with name {student} forgot how the f-format string works in {course}'
# # print(temp)
# "9- check if item exists in the dict "
# d = {
#     "track":"devops",
#     "courses":["django", 'python'],
#     "intake": {
#         "no": 43,
#         "Round":1
#     }
# }
#
# print(d)
#
# # if 'devops' in d:  # check if the value exists in the keys
# #     print('found')
# # else:
# #     print("not found")
#
# #
# # if 'devops' in d.values():  # check if the value exists in the keys
# #     print('found')
# # else:
# #     print("not found")


"10- update the dictionary"
d1 = {"name":"Mohamed", 'track':'devops', 'intake': '43'}
content= {
    "devlopment":["python", 'django'],
    'devops': ["docker",'jenkins', 'terraform'],
    'name':'test'
}
print(d1)
print(content)
d1.update(content)
print(d1)

d1.update(content)  # update key-value pairs of d1 with the key value pairs of content
# print(d1)
# print(content)


"11- remove key value pair from the dictionary"
# popped=d1.pop("devlopment") # retrun with the popped values

# d1.clear()  ### remove all the key value pairs in the dict

"12 --- del function"
del d1  # remove the dictionary form the memory

del content["devlopment"]  # delete this value pair from the dictionary
# return with None















