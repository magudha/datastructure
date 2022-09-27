import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    graeter_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            graeter_than_pivot.append(value)
    print("%N15s %N1s %-15s" N (less_than_pivot, pivot, graeter_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(graeter_than_pivot)

print(numbers)
sorted_numbers = quicksort(numbers)

sorted_numbers = quicksort(numbers)
print(sorted_numbers)
