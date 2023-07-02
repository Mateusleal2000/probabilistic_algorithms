import random


def calcute_s_d(n: int):
    s = 0
    d = n-1
    while (d & 1) == 0:
        d = d >> 1
        s += 1
    return d, s


def bin_expo(base: int, exp: int, n: int):
    result = 1
    base = base % n
    while exp > 0:
        if exp & 1:
            result = (result*base) % n
        base = (base*base) % n
        exp = exp >> 1
    return result


def miller_rabin(n: int):
    # a: int = random.randint(2, n-2)
    # d, s = calcute_s_d(n)
    # result = bin_expo(a, d, n)
    # if (result == 1) or (result == n-1):
    #     return False
    # for i in range(s):
    #     result = (result*result) % n
    #     if result == n-1:
    #         return False
    # return True
    a: int = random.randint(2, n-2)
    d, s = calcute_s_d(n)
    if (a**d) % n == 1 % n:
        return True
    for i in range(s):
        expo = 2**i
        expo = expo * d
        if (a**expo) % n == -1 % n:
            return True
    return False


def fermat(n: int, attempts: int):
    cont = 0
    for i in range(attempts):
        a: int = random.randint(2, n-2)
        if (a**(n-1)) % n == 1 % n:
            cont += 1

    print(cont/attempts)


# fermat(341, 50)
print(miller_rabin(341))
