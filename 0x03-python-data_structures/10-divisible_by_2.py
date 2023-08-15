#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiplesoftwo = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiplesoftwo.append(True)
        else:
            multiplesoftwo.append(False)

    return (multiplesoftwo)
