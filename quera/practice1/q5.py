"""
Author: Mohammad Nasiri
Ref: https://quera.org/course/assignments/57829/problems/196900
"""

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
factorial = 1
for i in range(1, num1+1):
    factorial = factorial*i

factorial_str = str(factorial)
res = [int(x) for x in str(factorial_str)]
print(res.count(num2))
