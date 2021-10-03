TC = int(input())

for tc in range(1, TC+1):
    nums = list(input())
    n = len(nums)
    base = ['0'] * n
    cnt = 0
    for x in range(n):
        if base[x] != nums[x]:
            # 그 뒤에는 똑같은거 다 입힘
            for y in range(x, n):
                base[y] = nums[x]
            cnt += 1
    print('#{} {}'.format(tc, cnt))