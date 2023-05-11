import random
import math
import matplotlib.pyplot as plt


def bernouli(p):
    if (random.random() <= p):
        return 0
    return 1


def buy_coupons(n, k):
    new_cards: int = 0
    p = 1.0 - pow(((n - 1)/n), k)
    for i in range(k):
        if bernouli(p) == 0:
            new_cards += 1
    return new_cards


def buy_coupons_package(n, k):
    new_cards: int = 0
    p = 1.0 - pow(((n - 1)/n), k)
    for i in range(k):
        if bernouli(p) == 0:
            new_cards += 1
    return new_cards


def buy_new_stamp(album):
    pos = random.randint(0, 679)
    if album[pos] == False:
        album[pos] = True
        return True, album
    return False, album


def buy_new_stamp_pack(album, pack_size):
    pos = random.sample(range(0, 679), pack_size)
    total_new_stamps = 0
    for val in pos:
        if album[val] == False:
            album[val] = True
            total_new_stamps += 1
    return total_new_stamps, album


def fill_album():
    n = 680
    k = 680
    album = [False for i in range(n)]
    new_stamps = 0
    for i in range(k):
        stamp_acquired, album = buy_new_stamp(album)
        if stamp_acquired:
            new_stamps += 1

    return new_stamps


def fill_album_pack():
    n = 680
    k = 680
    pack_size = 5
    album = [False for i in range(n)]
    new_stamps = 0
    total = 0
    while total != k:
        stamps_acquired, album = buy_new_stamp_pack(album, pack_size)
        total += pack_size
        if (total > k):
            total = k
        new_stamps += stamps_acquired

    return new_stamps


def execute():

    sum = 0
    sd_list = []
    mean = 0.0
    standard_deviation = 0.0
    for i in range(5000):
        value = fill_album()
        sd_list.append(value)
        sum += value
    mean = sum/5000.0
    for val in sd_list:
        standard_deviation += pow((val - mean), 2)
    return mean, math.sqrt(standard_deviation/5000.0), sd_list


def execute2():
    n = 680
    k = 680
    sum = 0
    sd_list = []
    mean = 0.0
    standard_deviation = 0.0
    for i in range(5000):
        value = fill_album()
        sd_list.append(value)
        sum += value
    mean = sum/5000.0
    for val in sd_list:
        standard_deviation += pow((val - mean), 2)
    return mean, math.sqrt(standard_deviation/5000.0), sd_list


# print("One stamp at a time")
# output1, output2, values_list = execute()
# print(f"Mean of new stamps: {output1}")
# print(f"Standard deviation: {output2}")
print("\n-----------------\n")
print("Buying coupons packages - 5 per package")
output3, output4, values_list2 = execute2()
print(f"Mean of new cards: {output3}")
print(f"Standard deviation: {output4}")

plt.hist(values_list2, bins=200)
plt.xlabel("Total of stamps bought")
plt.ylabel("Occurrences")
plt.show()
