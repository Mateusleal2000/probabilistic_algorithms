import random
import matplotlib.pyplot as plt
import numpy as np


def estimate_numpy(iterations: int):
    circle_dots = 0.0
    square_dots = 0.0
    x = np.random.uniform(0, 1, iterations)
    y = np.random.uniform(0, 1, iterations)
    for val_x, val_y in zip(x, y):
        if (((val_x-0.5)**2) + ((val_y-0.5)**2)) <= 0.25:
            circle_dots += 1
        square_dots += 1
    return 4*(circle_dots/square_dots)


def estimate(iterations: int):
    circle_dots = 0.0
    square_dots = 0.0
    pi_estimation = 0.0

    for i in range(0, iterations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if (x**2 + y**2) <= 1:
            circle_dots += 1
        square_dots += 1
        pi_estimation = 4*(circle_dots/square_dots)
    return pi_estimation


results = np.array([])
iter = np.array([])
for i in range(1000, 5000000, 10000):
    results = np.insert(results, results.size, estimate_numpy(i))
    print(i)
    iter = np.insert(iter, iter.size, i)
print(f"result: {results[results.size-1]}")

plt.plot(results, iter, "bo")
plt.xlim([3.12, 3.17])
plt.xlabel("Estimated Value")
plt.ylabel("Total of iterations")
plt.title("Monte Carlo Pi Simulation")

plt.show()
