import numpy as np
import random
import matplotlib.pyplot as plt
from time import perf_counter


def expected_time(n: int):
    return (n + 2) * (n - 1)


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
expected_times = []
elements_qty = []
for i in range(3, 101):
    elements_qty.append(i)
    execution_times.append(mcmc(i))
    expected_times.append(expected_time(i))


plt.plot(elements_qty, execution_times)
plt.plot(elements_qty, expected_times)
plt.xlabel("Quantity of elements")
plt.ylabel("Execution Time")
plt.show()

# for val in execution_times:
#     print(val)
