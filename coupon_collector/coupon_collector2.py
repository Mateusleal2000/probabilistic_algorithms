import random
import math


def bernouli(p):
    if (random.random() <= p):
        return 0
    return 1


def buy_coupons(n, k):
    new_cards: int = 0
    p = 1.0 - pow(((n - 1)/n), k)
    for i in range(k):
        if bernouli(p) == 0:
            new_cards += 1
    return new_cards


def buy_coupons_package(n, k):
    new_cards: int = 0
    p = 1.0 - pow(((n - 1)/n), k)
    for i in range(k):
        if bernouli(p) == 0:
            new_cards += 1
    return new_cards


def execute():
    n = 680
    k = 680
    sum = 0
    sd_list = []
    mean = 0.0
    standard_deviation = 0.0
    for i in range(5000):
        value = buy_coupons(n, k)
        if i < 50:
            print(value)
        sd_list.append(value)
        sum += value
    mean = sum/5000.0
    for val in sd_list:
        standard_deviation += pow((val - mean), 2)
    return mean, math.sqrt(standard_deviation/5000.0), sd_list


def execute2():
    n = 680
    k = 680
    sum = 0
    sd_list = []
    mean = 0.0
    standard_deviation = 0.0
    for i in range(5000):
        value = buy_coupons_package(n, k)
        sd_list.append(value)
        sum += value
    mean = sum/5000.0
    for val in sd_list:
        standard_deviation += pow((val - mean), 2)
    return mean, math.sqrt(standard_deviation/5000.0), sd_list


print("One coupon at a time")
output1, output2, values_list = execute()
print(f"Mean of new cards: {output1}")
print(f"Standard deviation: {output2}")
print("\n-----------------\n")
print("Buying coupons packages - 5 per package")
output3, output4, values_list2 = execute2()
sum: float = 0.0
for value in values_list2:
    sqr = (value - (680*(1 - (1/math.e))))
    sum = sum + (sqr*sqr)
output4 = math.sqrt(sum/5000)
print(f"Mean of new cards: {output3}")
print(f"Standard deviation: {output4}")
