import random

circle_dots = 0.0
square_dots = 0.0
pi_estimate = 0.0
results = []

for i in range(0, 5000000):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if (x**2 + y**2) <= 1:
        circle_dots += 1
    square_dots += 1
    pi_estimate = 4*(circle_dots/square_dots)
    results.append(pi_estimate)


sum = 0.0
for i in range(len(results)):
    sum = results[i] + sum

print(sum/len(results))
