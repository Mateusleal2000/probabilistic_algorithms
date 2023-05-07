import random
import math


def geom_dist(p: float) -> int:
    counter: int = 0
    while random.random() > p:
        counter += 1
    counter += 1
    return counter


def check_package(package, owned_coupons, total_coupons):
    for coupon in package:
        p: float = (total_coupons - owned_coupons)/total_coupons
        if coupon < p:
            owned_coupons += 1
    return owned_coupons


def collectors_problem() -> float:
    total_coupons: int = 680
    total_bought: int = 0
    for i in range(total_coupons):
        p: float = (total_coupons - i)/total_coupons
        total_bought = geom_dist(p) + total_bought
    return total_bought


def collectors_problem_packs() -> float:
    total_coupons: int = 680
    pack_size: int = 5
    total_bought: int = 0
    new_coupons: int = 0
    while total_coupons != new_coupons:
        package = [random.random(), random.random(), random.random(),
                   random.random(), random.random()]
        new_coupons = check_package(package, new_coupons, total_coupons)
        total_bought += 5
        if new_coupons > total_coupons:
            new_coupons = total_coupons

    return total_bought


def execute():
    mean: float = 0.0
    standard_deviation: float = 0.0
    sum: float = 0.0
    sd_list: float = []
    for i in range(5000):
        val: float = collectors_problem()
        sd_list.append(val)
        sum = sum + val
    mean = sum/5000
    for value in sd_list:
        standard_deviation += pow((value - mean), 2)
    return mean, math.sqrt(standard_deviation/5000)


def execute2():
    mean: float = 0.0
    standard_deviation: float = 0.0
    sum: float = 0.0
    sd_list: float = []
    for i in range(5000):
        val: float = collectors_problem_packs()
        sd_list.append(val)
        sum = sum + val
    mean = sum/5000
    for value in sd_list:
        standard_deviation += pow((value - mean), 2)
    return mean, math.sqrt(standard_deviation/5000)


print("Buying one card at a time")
output1, output2 = execute()
print(f"Mean: {output1}")
print(f"Standard Deviation: {output2}")


print("Buying packages with 5 different cards each")
output3, output4 = execute2()
print(f"Mean: {output3}")
print(f"Standard Deviation: {output4}")
