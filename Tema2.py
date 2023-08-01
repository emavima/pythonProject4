# Note: listA and listB are always sorted

def merge(listA, listB):
    newList = []

    i = 0
    j = 0

    while i < len(listA) and j < len(listB):
        if listA[i] < listB[j]:
            newList.append(listA[i])
            i += 1
        else:
            newList.append(listB[j])
            j += 1




    if len(listA) > i:
        newList.extend(listA[i:])
    if len(listB) > j:
        newList.extend(listB[j:])





    return newList


def printExample2(listA, listB):
    print(f"mfync2{listA, listB} = {merge(listA, listB)}")


#printExample2([1, 2], [3, 4])
#printExample2([2, 3], [1, 4])
printExample2([2, 4], [1, 3])