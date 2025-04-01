a = [4, 6, 5, 3, 3, 1]

max_sub = 0
for i in set(a):
    test = [num - i for num in a if num - i <= 1]
    up = sum([(num in [0, 1]) for num in test])
    down = sum([(num in [0, -1]) for num in test])
    print(i)
    print(test)
    print(up)
    print(down)
    print("-"*10)
    if max(up, down) > max_sub:
        max_sub = max(up, down)