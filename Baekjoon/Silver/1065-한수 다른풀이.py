import sys
sys.stdin = open('1065-백준-한수.txt')

TC = 4
for tc in range(1, TC+1):
    num = int(input())

    cnt = 0

    for n in range(1, num+1):
        if n <= 99:
            cnt += 1
        else:
            nums = list(map(int, str(n)))   # 이게 핵심!!!!
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1
    print(cnt)