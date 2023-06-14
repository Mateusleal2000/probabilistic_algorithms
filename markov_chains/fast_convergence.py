import numpy as np
import random
import matplotlib.pyplot as plt
from time import perf_counter


def fast_convergence(n: int):
    # pi_i = np.full((1, n+1), 1/(n+1))
    pi_i = [1/(n+1)]*(n+1)
    for j in range(60):
        for i in range(len(pi_i)):
            aux = 0
            if i == 0:
                aux = pi_i[i]/2 + pi_i[i+1]/2
            elif i == len(pi_i)-1:
                aux = pi_i[i-1]/2
            elif i == len(pi_i)-2:
                aux = pi_i[i-1]/2
            else:
                aux = pi_i[i-1]/2 + pi_i[i+1]/2
            pi_i[i] = aux
    return (1/pi_i[n])-1


def expected_time(n: int):
    return (n + 2) * (n - 1)


t_nn = []
elements_qty = []
expected_times = []
for i in range(3, 101):
    t_nn.append(fast_convergence(i))
    elements_qty.append(i)
    expected_times.append(expected_time(i))

# fast_convergence(5)

plt.plot(elements_qty, t_nn)
plt.plot(elements_qty, expected_times)
plt.xlabel("Quantity of elements")
plt.ylabel("Execution Time")
plt.show()
