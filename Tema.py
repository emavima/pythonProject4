lst = [1, 2, 3, 4]
lst_1 = [1, 1, 1, 1]
def cumulative(lst):

    new_lst = []

    cumulative_sum = 0

    for number in lst:

        cumulative_sum += number


        new_lst.append(cumulative_sum)


    return new_lst




print(cumulative(lst))
print(cumulative(lst_1))
