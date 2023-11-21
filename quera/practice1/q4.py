"""
Author: Mohammad Yazdani
Ref: https://quera.org/course/assignments/57829/problems/196761
"""

def chocolate_milk():
    number_of_kids = int(input())
    require = input().split(" ")
    require = tuple(map(int, require))
    total = 0
    need = 0
    for i in range(number_of_kids):
        if require[i] > 0:
            if total >= require[i]:
                total -= require[i]
            else:
                need += require[i] - total
                total = 0
        else:
            total += abs(require[i])

    print(need)

chocolate_milk()