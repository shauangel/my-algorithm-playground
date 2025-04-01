def getTotalX(a, b):
    # Write your code here
    # Find considered integer
    cnt = 0
    for i in range(min(a), min(b)+1):
        test = True
        for j in a:
            if i%j != 0:
                test = False
                break
        if not test:
            continue
        else:
            for j in b:
                if j%i !=0:
                    test=False
                    break
        if test:
            cnt+=1
            print(i)
    return cnt


if __name__ == "__main__":
    a = [2, 4]
    b = [16, 32, 96]
    print(getTotalX(a, b))