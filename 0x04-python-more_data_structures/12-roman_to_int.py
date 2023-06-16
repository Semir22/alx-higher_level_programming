#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    list = [roman_num[x] for x in roman_string]
    num = 0
    for i in range(len(list)):
        num += list[i]
        if list[i - 1] < list[i] and i != 0:
            num -= (list[i - 1] + list[i - 1])
    return num
