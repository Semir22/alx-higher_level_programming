#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
	comp_num = "and is greater than 5"
elif last_digit == 0:
	comp_num = "and is 0"
else:
	comp_num = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {comp_num}")
