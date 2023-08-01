lst = [1, 2, 3, 2, 4, 1, 5, 6, 5]

def duplicates_remover(lst):

    lst1 = []

    dict = {}

    for number in lst:

        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1


    for number in dict:
        if dict[number] == 1:
            lst1.append(number)




    return lst1



print(duplicates_remover(lst))