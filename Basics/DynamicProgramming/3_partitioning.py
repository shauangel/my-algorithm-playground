"""
<<Problem>>
Given a set of numbers s = {s_1, ..., s_n}
Check if it can partition into two set I, J, K
where sum(I) = sum(J) = sum(K) = 1/3 * sum(s) (target)

<<DP Statement>>
Sub-Problem:
Given subset of s, where s_i = {s_1, ..., s_i}, check if there exist some subset
that can form into three sets with sum x, y
DP[x][y] = True, if exist some subsets that forms subset with sum x and y

Base Case: (x, y = 0, always true with no items considered)
DP[0][0] = True

Recurrence:
if exist a valid set for sum x, y, try to expand the sets
(1) if x + num <= target, DP[x+num][y] = True
(1) if y + num <= target, DP[x][y+num] = True

Output:
DP[target][target]
"""
import numpy as np


def three_partitioning(s):
    # Check immediate stop statement
    if sum(s) % 3 != 0:
        print("not satisfy")
        return False

    # Initialize dp
    target = sum(s)//3
    dp = np.zeros(shape=(target+1, target+1), dtype=bool)
    dp[0][0] = True

    for num in s:
        # same as 2 partition
        for x in range(target, -1, -1):
            for y in range(target, -1, -1):
                if dp[x][y]:
                    if x+num <= target:
                        dp[x+num][y] = True
                    if y+num <= target:
                        dp[x][y+num] = True
        print(dp)
    return dp[target][target]


if __name__ == "__main__":
    test1 = [2, 2, 3, 4, 4, 5, 7]
    test2 = [2, 2, 3, 5]
    inst = three_partitioning(test2)
    print(inst)