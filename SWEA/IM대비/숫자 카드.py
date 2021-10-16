import sys
sys.stdin = open('숫자 카드.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input()))
    max_num = max(nums)
    counting = [0] * (max_num+1)
    for x in nums:
        counting[x] += 1

    max_id = 0
    max_num = 0
    for y in range(len(counting)):
        if counting[y] >= max_num:
            max_num = counting[y]
            max_id = y

    print('#{} {} {}'.format(tc, max_id, max_num))
