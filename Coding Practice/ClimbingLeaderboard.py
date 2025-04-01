"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

def search_score(arr, num, s, e):
    # print(f"start: {s}, end: {e}")
    # print(arr[s:e])
    if abs(s-e) <= 1:
        if num < arr[e]: return len(arr)+1
        if num >= arr[s] and s==0: return 1
        return e+1
    mid = int( (s + e) / 2)
    if arr[mid] == num: return mid+1
    elif arr[mid] < num:
        return search_score(arr, num, s, mid)
    else:
        return search_score(arr, num, mid, e)



if __name__ == "__main__":
    # ranked = [100, 90, 90, 80, 75, 60]
    # player = [50, 65, 77, 90, 102]

    ranked = [100, 100, 50, 40, 40, 20, 10]
    # player = [5, 25, 50, 120]
    player = [5]

    uniq = sorted(list(set(ranked)), reverse=True)
    # print(uniq)
    for i in player:
        print(search_score(uniq, i, 0, len(uniq)-1))