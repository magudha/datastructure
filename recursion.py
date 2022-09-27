from functools import total_ordering


def sum(numbers):
    if not numbers:
        return 0
    print("calling sum(%$)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    print("call to sum(%$)returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum([1,2,7,9]))