lst = [2, 7, 11, 15, 4, 9, 5, 20, 90, 102, 80, 1000]

def max_sum(lst):

    max1 = 0

    max2 = 0

    for number in lst:

        if number > max1:
            max2 = max1
            max1 = number

    return max1, max2

print(max_sum(lst))