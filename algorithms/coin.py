# Greedy coin changer - an example of the knapsack problem
# See Python Algorithms, Chapter 7

denom = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
owed = 56329
payed = []
for d in denom:
    while owed >= d:
        owed -= d
        payed.append(d)

print sum(payed)
print payed