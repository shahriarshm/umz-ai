"""
Author: Fateme Amlahi
Ref: https://quera.org/course/assignments/58165/problems/197469
"""

def pythagoras(a,b,c):
    if a**2==b**2+c**2 or b**2 == a**2 +c**2 or c**2==a**2+ b**2:
        print("YES")
    else:
        print("NO")
    
a=int(input())
b=int(input())
c=int(input())
pythagoras(a,b,c)