#!/usr/bin/python3
"""a funtion that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds the peak in a ist of unsorted integers"""
    mylist = list_of_integers
    if mylist == []:
        return None
    length = len(mylist)
    first, last = 0, length - 1
    while first < last:
        mid = first + (last - first) // 2
        if mylist[mid] > mylist[mid - 1] and mylist[mid] > mylist[mid + 1]:
            return mylist[mid]
        if mylist[mid - 1] > mylist[mid + 1]:
            last = mid
        else:
            first = mid + 1
    return mylist[first]
