def solution(arr):
    ans = []
    for x in range(len(arr)-1):
        if arr[x] != arr[x+1]:
            ans.append(arr[x])
    ans.append(arr[-1])
    return ans