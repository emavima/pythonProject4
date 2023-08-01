str_ = "mississippi"

def most_occurences(str):

    lst = []

    for char in range(len(str) - 1):

        item_pair = str[char:char+2]

        lst.append(item_pair)

    dict = {}

    for char in lst:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] = dict[char] + 1


    return max(dict, key = lambda key: dict[key])


print(most_occurences(str_))