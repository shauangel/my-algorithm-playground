def mergeSort(S):
    if len(S) <= 1:
        return S
    s1 = mergeSort(S[:len(S)/2+1])
    s2 = mergeSort(S[len(S)/2+1:])
    return


def merge2sortedArr(s1, s2):
    result = []
    try:
        while len(s1) > 0 or len(s2) > 0:
            print(s1)
            print(s2)
            print("-"*10)
            try:
                if s1[0] < s2[0]:
                    result.append(s1[0])
                    del s1[0]
                else:
                    result.append(s2[0])
                    del s2[0]
            except IndexError:
                if len(s1) > 0:
                    result.append(s1[0])
                    del s1[0]
                else:
                    result.append(s2[0])
                    del s2
    except UnboundLocalError:
        return result
    return result


if __name__ == "__main__":
    a = [3, 27, 38, 43]
    b = [9, 10, 82]

    print(merge2sortedArr(a, b))