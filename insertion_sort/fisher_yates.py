import numpy as np
import random
from time import perf_counter


def fisher_yates_shuffle(n: int):
    shuffled_list = np.arange(n)
    for i in range(n):
        l = random.randint(i, n-1)
        aux = shuffled_list[l]
        shuffled_list[l] = shuffled_list[i]
        shuffled_list[i] = aux

    return shuffled_list


def insertion_sort(shuffled_list: np.array):
    n = shuffled_list.size
    number_of_comparisons = 0
    start = perf_counter()
    for k in range(1, n):
        val = shuffled_list[k]
        j = k-1
        while j >= 0 and val < shuffled_list[j]:
            number_of_comparisons += 1
            shuffled_list[j+1] = shuffled_list[j]
            j -= 1
        shuffled_list[j+1] = val
    end = perf_counter()
    return shuffled_list, number_of_comparisons/n, end-start


def probabilistic_insertion_sort(n: int):
    shuffled_list = fisher_yates_shuffle(n)
    print(shuffled_list)
    return insertion_sort(shuffled_list)


array_size = []
times = []
proportions = []
for i in range(100, 800, 10):
    ordered_list, proportion, time_duration = probabilistic_insertion_sort(i)
    proportions.append(proportion)
    times.append(time_duration)
    array_size.append(i)


# print("After calling probabilistic insertion sort:")
# print(ordered_list)
# print(proportion)
# print(time_duration)
