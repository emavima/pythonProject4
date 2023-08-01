from Tema2 import merge

lst = [1, 2, 3, 2, 4, 1, 5, 6, 5]
def mergesort(lst):

    if len(lst) <= 1:
        return lst

    lst1 = lst[:len(lst) // 2]

    lst2 = lst[len(lst) // 2:]


    lst1 = mergesort(lst1)
    lst2 = mergesort(lst2)

    #return merge(lst1, lst2)

#print(mergesort(lst))