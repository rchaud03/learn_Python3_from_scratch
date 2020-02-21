list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_common = []

#for i in list_a and j in list_b:
for i in list_a:

    if i in list_b and i not in list_common:
        list_common.append(i)
print(list_common)