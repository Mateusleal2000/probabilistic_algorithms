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


def execute():
    n = 680
    k = 680
    sd_list = []
    mean = 0.0
    standard_deviation = 0.0
    for i in range(5000):
        value = buy_coupons(n, k)
        sd_list.append(value)
        mean += value
    mean /= 5000
    for val in sd_list:
        standard_deviation = standard_deviation + pow((val-mean), 2)
    standard_deviation /= 5000
    return mean, math.sqrt(standard_deviation), sd_list


mean, standard_deviation, sd_list = execute()
print(f"Mean of new cards: {mean}")
print(f"Standard deviation: {standard_deviation}")
