def iterative_F(n):
    if n==0:
        return 0
    Fn = [0]*(n+2)
    Fn[0] = 0
    Fn[1] = 1
    for i in range(2, n+1):
        Fn[i] = Fn[i-1] + Fn[i-2]
    return Fn[n]

print(iterative_F(15))