def solution(arr, divisor):
    ans = []
    for x in arr:
        if x % divisor == 0:
            ans.append(x)
    ans.sort()

    if len(ans) == 0:
        return [-1]
    else:
        return ans