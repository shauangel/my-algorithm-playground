"""
Definition: Magic matrix
All rows, columns and diagonals have same sum (magic constant)

Generate 3x3 magic matrix by Édouard Lucas's formula:
| c-b   | c+a+b | c-a   |
| c-a+b | c     | c+a-b |
| c+a   | c-a-b | c+b   |
thus, for numbers [1-9], we can use these 8 pairs of (a, b) to generate different matrix:
(3, 1), (3, -1), (-3, 1), (-3, -1), (1, 3), (1, -3), (-1, 3), (-1, -3)
"""
import itertools

test_1 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 5]
]

test_2 = [
    [5, 3, 4],
    [1, 5, 8],
    [6, 4, 2]
]

a = [3, -3]
b = [1, -1]
num_pairs = list(itertools.product(a, b)) + list(itertools.product(b, a))
min_cost = 100
for i in range(8):
    a = num_pairs[i][0]
    b = num_pairs[i][1]
    magic_mat = [
        [5-b, 5+a+b, 5-a],
        [5-a+b, 5, 5+a-b],
        [5+a, 5-a-b, 5+b]
    ]
    sum = 0
    for r in range(3):
        for c in range(3):
            sum+= abs(magic_mat[r][c]-test_2[r][c])
    if sum < min_cost:
        min_cost = sum
print(min_cost)



