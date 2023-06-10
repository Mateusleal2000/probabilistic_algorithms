import numpy as np
import random
import matplotlib.pyplot as plt
from time import perf_counter


def mcmc(n: int):
    repetitions = 1000
    x = 1
    time_total = 0

    for i in range(repetitions):
        x = 1
        time = 0
        while x != n:
            time += 1
            p = random.random()
            if x == 0:
                if p < 0.5:
                    x = 1
            elif x > 0:
                if p < 0.5:
                    x -= 1
                else:
                    x += 1
        time_total += time

    return time_total/repetitions


execution_times = []
for i in range(3, 101):
    execution_times.append(mcmc(i))


for i in range(10):
    print(execution_times[i])
