import numpy as np

def fisher_yates_shuffle(n):
    shuffled_list = np.random.randint(n, size=n)
    
    return shuffled_list

def insertion_sort(shuffled_list):
    #insertion sort algorithm
    return 0

def probabilistic_insertion_sort():
    shuffled_list = fisher_yates_shuffle()
    insertion_sort(shuffled_list)
    return 0
