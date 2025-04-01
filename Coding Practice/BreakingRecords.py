import itertools


def birthday(s, d, m):
    # Write your code here
    satisfy = []
    for i in itertools.combinations(s, m):
        if sum(i) == d:
            if i not in satisfy:
                satisfy.append(i)
    return len(satisfy)


s = [1, 2, 1, 3, 2]
d = 3
m = 2

print(birthday(s, d, m))
