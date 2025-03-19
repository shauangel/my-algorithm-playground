"""
Try every single
"""


"""
n = length of P, m = length of T
Time Complexity: O((m-n+1)*n) = O(mn)
"""
def brute_force(P, T):
    offsets = []
    match_count = 0
    for i in range(len(T)-len(P)+1):
        match = True
        for l in range(len(P)):
            match_count+=1
            if P[l] != T[i+l]:
                match = False
                break
        if match:
            offsets.append(i)
    print(match_count)
    return offsets

"""
Let x = |P|, y = |T|
Question: How many possible alignments for given x, y?
Ans: y-x+1
Question: What is the max times of checking characters?
Ans: (y-x+1)*x
Question: What is the least times of checking characters?
Ans: y-x+1 (when missed at the first char everytime)

--> In practice: the running time is closer to the min case
"""
def skip_bruteforce(P, T):
    offsets = []
    match_count = 0
    i = 0
    while i < len(T)-len(P)+1:
        i += 1
        match = True
        for l in range(len(P)):
            match_count += 1
            if P[l] != T[i+l]:
                match = False
                i += l   # skip compared letters
                break
        if match:
            offsets.append(i)
    print(match_count)
    return offsets



if __name__ == "__main__":
    P = "word"
    T = "afebisdbflkwordsibdfaswoobi29306weworhflxcword"
    print(brute_force(P, T))

    print(skip_bruteforce(P, T))