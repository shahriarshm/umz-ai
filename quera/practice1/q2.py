"""
Author: Moein Ghasemi
Ref: https://quera.org/course/assignments/57829/problems/196904
"""

inv_c = 0


def mergeSort(array):
    n = len(array)
    if n == 1:
        return array
    L = mergeSort(array[:round(n/2)])
    R = mergeSort(array[round(n/2):n])
    return mergePieces(L, R)


def mergePieces(L, R):
    i = 0
    j = 0
    returnValue = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            returnValue.append(L[i])
            i += 1
        else:
            returnValue.append(R[j])
            global inv_c
            j += 1
            inv_c += len(L) - i

    while i < len(L):
        returnValue.append(L[i])
        i += 1
    while j < len(R):
        returnValue.append(R[j])
        j += 1
    return returnValue


n = int(input(""))
numbers = []
for i in range(n):
    num = int(input(""))
    numbers.append(num)
# numbers = [2,3,1]
mergeSort(numbers)
print(inv_c % 100000)