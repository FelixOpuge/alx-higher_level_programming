#!/usr/bin/python3
for num in range(10):
    for num1 in range(10):
        if num1 > num and num != 8:
            print(f"{num:d}{num1:d}", end=", ")
        elif num == 8 and num1 == 9:
            print(f"{num:d}{num1:d}")
            break
