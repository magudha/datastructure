# Program to print positive Num

from tracemalloc import start


start, end = 0, 10000

# Iterate each number in list
for num in range(start, end + 1):
    # Checking condition
    if num >= 0:
        print(num, end = "")