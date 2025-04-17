"""
<<Problem>>
Given a sequence of cannonballs X = {x_1, ..., x_n} within n seconds
An EMP is used to destroy cannonballs, which destroy min{x_k, f(j)} cannonballs
in the kth second and has the interval time of j seconds.
Find the maximum number of cannonballs it can destroy.

<<Dp Statements>>
* Sub-problem Definition
Find the maximum nuber of cannonballs that EMP can destroy from 1 to i
DP[i] = max # of cannonballs destroy

* Recurrence Relation
(case 1): EMP not used DP[i] = DP[i-1]
(case 2): Used EMP DP[i] = max{ for all k in 1...i, DP[k-1] + min{x_i-1, f(i-k+1)} }

* Base Case
No cannonballs, thus, no destruction
DP[0] = 0

* Output
DP[n]
"""
import numpy as np


def func(j):
    return 2 * j if j >= 1 else 0


def max_destroy(x, f):
    n = len(x)
    dp = np.zeros(shape=(n+1), dtype=int)

    for idx in range(1, n+1):
        # Calculate all possible interval
        dp[idx] = dp[idx-1]
        print(idx)
        for k in range(0, idx):
            dp[idx] = max(dp[idx], dp[k-1] + min(x[idx-1], func(idx - k + 1)))
            print(dp)
    return dp[n]


if __name__ == "__main__":
    x = [4, 2, 7, 1, 8, 3]
    print(max_destroy(x, func))
