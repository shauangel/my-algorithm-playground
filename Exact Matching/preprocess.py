

def fundamental_preprocess(S):
    Z = []
    for i in range(1, len(S)):
        z_cnt = 0
        for j in range(len(S)-i):
            if S[j] == S[i+j]:
                z_cnt+=1
            else:
                break
        Z.append(z_cnt)
    return Z


"""
Variables:
Z: the match # of prefix
r: current right endpoint of z-boxes
l: current left endpoint of z-boxes
"""
def linear_preprocess(S):
    # 0. Initialize Z, r, l
    Z = []
    r = 0
    l = 0
    # 1. find Z2
    z2 = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            z2 += 1
        else:
            break
    Z.append(z2)
    if z2 > 0:
        r = z2 + 1
        l = 2

    # 3. iterate through all chracter
    for i in range(1, len(S)):
        break


if __name__ == "__main__":
    test = "aabaaabaabaaaabababaaa"
    print(fundamental_preprocess(test))

