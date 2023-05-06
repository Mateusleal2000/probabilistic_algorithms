import random


def geom(p: float) -> int:
    counter: int = 0
    while random.random() > p:
        counter += 1
    counter += 1
    return counter


def collectors_problem() -> float:
    total_coupons: int = 680
    total_bought: int = 0
    for i in range(total_coupons):
        p: float = (total_coupons - i)/total_coupons
        total_bought = geom(p) + total_bought
    return total_bought


def execute():
    mean: float = 0.0
    standard_deviation: float = 0.0
    sum: float = 0.0
    for i in range(5000):
        sum = sum + collectors_problem()
    mean = sum/5000
    return mean, standard_deviation


output1, output2 = execute()
print(f"Mean: {output1}")
print(f"Standard Deviation: {output2}")
