"""
Ref: https://quera.org/course/assignments/58165/problems/197468
"""

n = int(input())
f = 1
for i in range(1,n+1) : 
    f *= i
print(f)