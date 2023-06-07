#!/usr/bin/python3
for i in range(8):
	for j in range(1, 10):
		if (i + j) < 10:
			print(f"{i}{i + j}", end=", ")
print("89")
