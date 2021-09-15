import sys
sys.stdin = open('2491-수열-백준.txt')

N = int(input())

nums = list(map(int, input().split()))
cnt = 1
max_cnt = 1
for num in range(N-1):
    if nums[num] <= nums[num+1]:
        cnt += 1
    else:
        cnt = 1

    if max_cnt < cnt:
        max_cnt = cnt
cnt_1 = 1
for num in range(N-1):
    if nums[num] >= nums[num+1]:
        cnt_1 += 1
    else:
        cnt_1 = 1
    if max_cnt < cnt_1:
        max_cnt = cnt_1
print(max_cnt)