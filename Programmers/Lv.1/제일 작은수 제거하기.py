def solution(arr):
    min_num = min(arr)
    ans = []
    if len(arr) == 1:
        ans.append(-1)
    for x in arr:
        if x != min_num:
            ans.append(x)
    return ans