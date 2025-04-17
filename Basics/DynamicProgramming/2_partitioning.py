"""
<<Problem>>
Given a set of numbers s = {s_1, ..., s_n}, check if it can partition into two set x, y,
where sum(x) = sum(y) = 1/2 * sum(s) (target)

<<DP Statement>>
Sub-Problem:
is there exists a subset that satisfy sum of t
DP[t] = True, if exists such set

Base Case: (0 numbers, sum to 0)
DP[0] = True

Recurrence:
for ith item a[i-1], we have two choice (1) exclude (2) include
(1) DP[t] = DP[t]
(2) DP[t] = DP[t - a[i-1]]
when to include?
t >= a[i-1] => subset y has more space to increase

Output:
DP[target]
"""
import numpy as np


def two_partitioning(s):
    # Check immediate stop statement
    if sum(s) % 2 != 0:
        print("not satisfy")
        return False

    # Initialize dp
    target = sum(s)//2
    dp = np.zeros(shape=(target+1), dtype=bool)
    dp[0] = True

    for num in s:
        # consider sum from backward to prevent consider num more than once
        for t in range(target, num-1, -1):
            dp[t] |= dp[t - num]
        print(dp)

    return dp[target]


if __name__ == "__main__":
    test1 = [1, 2, 3, 4, 5, 6]
    test2 = [2, 2, 4, 4, 6]
    inst = two_partitioning(test2)
    print(inst)