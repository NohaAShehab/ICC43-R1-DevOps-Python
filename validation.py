print("--------------- welcome to validation moduleee--------------")

pi = 3.14
def askfornum():
    num = input("please enter number .. ")
    if num.isdigit():
        num = int(num)
        return num

    print("please enter valid number ")
    return askfornum()  # recursion


# askfornum()