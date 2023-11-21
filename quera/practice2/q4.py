"""
Author: Ali Ramezani
Ref: https://quera.org/course/assignments/58165/problems/197472
"""

n = list(map(int, input().split()))
heights = list(map(int, input().split()))

peoples = n[0]
max_dist = n[1]
max_height = max(heights)
justice_dist = 0

for height in heights:
    if max_height - height > max_dist:
        justice_dist += (max_height - height - max_dist)

print(justice_dist)

