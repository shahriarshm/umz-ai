"""
Author: Ebrahim Ebrahimi
Ref: https://quera.org/course/assignments/57829/problems/196760
"""

new_n, new_k = map(int, input().split())
new_a = list(map(int, input().split()))
new_d = [0] * new_n

def calculate_distance(a,b):
    if a <= b:
        return b - a
    return new_k-(a-b)

new_d[new_n - 1] = 0
for i in range(new_n - 2, -1, -1):
    new_d[i] = calculate_distance(new_a[i],new_a[i + 1]) + new_d[i + 1]

for i in range(new_n):
    print(new_d[i] + new_a[i])
