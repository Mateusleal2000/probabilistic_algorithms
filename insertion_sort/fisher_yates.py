import numpy as np
import random


def fisher_yates_shuffle(n: int):
    shuffled_list = np.arange(n)
    for i in range(n):
        l = random.randint(i, n-1)
        aux = shuffled_list[l]
        shuffled_list[l] = shuffled_list[i]
        shuffled_list[i] = aux

    return shuffled_list


def insertion_sort(shuffled_list):
    # insertion sort algorithm
    return 0


def probabilistic_insertion_sort(n: int):
    shuffled_list = fisher_yates_shuffle(n)
    insertion_sort(shuffled_list)
    return 0
