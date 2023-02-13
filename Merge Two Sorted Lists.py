def mergeTwoLists(list1: list, list2: list):
    list1.extend(list2)
    list1.sort()
    return list1


lst1 = [1, 2, 4]
lst2 = [1, 3, 4]
print(mergeTwoLists(lst1, lst2))
