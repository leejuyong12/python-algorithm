def cal(nums):
    ST = []
    cnt = 1
    while nums[-1] > 0:
        ST.append(nums.pop(0))
        nums.append(ST[-1] - cnt)
        if cnt == 5:
            cnt = 1
            continue
        cnt += 1
    nums.pop(-1)
    nums.append(0)
    return nums


TC = 10
for tc in range(1, TC + 1):
    tm = int(input())
    nums = list(map(int, input().split()))

    a = cal(nums)
    result = ''
    for x in a:
        result += (str(x) + ' ')

    print('#{} {}'.format(tc, result))