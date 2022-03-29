import sys
sys.stdin = open('단어수학.txt')


N = int(input())
res = 0
dic = {}
nums = [list(input()) for _ in range(N)]
nums.sort(reverse=True, key=len)    # key=len으로 하면 길이에 따라 정렬
for i in range(N):
    for j in range(len(nums[i])):
        if nums[i][j] not in dic.keys():
            dic[nums[i][j]] = 9 - len(dic)
ans = 0
for i in range(N):
    tmp = ''
    for j in range(len(nums[i])):
        tmp += str(dic[nums[i][j]])
    ans += int(tmp)
print(dic)