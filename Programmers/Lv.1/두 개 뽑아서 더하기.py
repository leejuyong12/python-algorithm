def solution(numbers):
    ans = []
    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            if (numbers[x] + numbers[y]) not in ans:
                ans.append(numbers[x] + numbers[y])
    ans.sort()
    return ans