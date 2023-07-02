import numpy as np
import matplotlib.pyplot as plt


def fast_convergence(n: int):
    p = 1/2
    q = 1-p

    matrix_P = np.zeros((n+1, n+1))
    matrix_P[0][0] = q
    matrix_P[0][1] = p
    matrix_P[n][1] = 1
    pi_i = [1/(n+1)]*(n+1)
    for i in range(1, n):
        matrix_P[i][i+1] = p
        matrix_P[i][i-1] = q

    final_pi = np.dot(pi_i, np.linalg.matrix_power(matrix_P, n*25))
    return (1/final_pi[n])-1


def expected_time(n: int):
    return (n + 2) * (n - 1)


t_nn = []
elements_qty = []
expected_times = []
for i in range(3, 101):
    t_nn.append(fast_convergence(i))
    elements_qty.append(i)
    expected_times.append(expected_time(i))


plt.plot(elements_qty, t_nn)
plt.plot(elements_qty, expected_times)
plt.xlabel("Quantity of elements")
plt.ylabel("Execution Time")
plt.show()
