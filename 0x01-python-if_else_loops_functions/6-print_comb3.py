#!/usr/bin/python3
for i in range(8):
    for j in range(1, 10):
        if (i + j) < 10:
            print("{:d}{:d}".format(i, j), end=', ')
print("{:d}{:d}".format(i + 1, j))
