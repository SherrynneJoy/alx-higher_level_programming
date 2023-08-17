#!/usr/bin/python3
def to_reduce(num_list):
    red = 0
    max_list = max(num_list)

    for m in num_list:
        if max_list > m:
            red += n
    return (max_list - red)

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V':5 , 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_keys = list(roman.keys())
    number = 0
    last_roman = 0
    num_list = [0]
    for ch in roman_string:
        for r_number in new_keys:
            if r_number == ch:
                if roman.get(ch) <= last_roman:
                    number += to_reduce(num_list)
                    num_list = [roman.get(ch)]
                else:
                    num_list.append(roman.get(ch))

                last_roman = roman.get(ch)
        number += to_reduce(num_list)
        return (number)
