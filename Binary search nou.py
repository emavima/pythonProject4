lst = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 16

def binary_search(lst, target):

    lower = 0

    upper = len(lst)

    while upper > lower:

        midpoint = (lower + upper)//2

        if target < lst[midpoint]:
            upper = midpoint
        elif target > lst[midpoint]:
            lower = midpoint + 1
        elif target == lst[midpoint]:
            return midpoint

    return None

for number in range(101):
    i = binary_search(lst, number)
    if number in lst:
        if lst[i] != number:
            raise Exception(f'lst[i] != number: lst[{i}] != {number}')
    else:
        if i is not None:
            raise Exception(f'Number {number} not in list, {i}')


print(binary_search(lst, target))
