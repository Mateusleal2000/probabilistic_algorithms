import random
import math


def A(r: int):
    return (r+1)*(r-2)*(r+3)*(r-4)


def B(r: int):
    return math.pow(r, 4)+(7*(r*r))-24


def poly_fingerprint(n: int):
    p = random.uniform(1, 100*n)
    if A(p) == B(p):
        return True
    return False


for i in range(100):
    if poly_fingerprint(4) == True:
        i = 100
        print("True")
