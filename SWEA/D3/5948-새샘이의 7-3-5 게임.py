TC = int(input())

for tc in range(1, TC+1):
    nums = list(map(int, input().split()))
    sum_num = []
    for x in range(len(nums)-2):
        for y in range(x+1, len(nums)-1):
            for z in range(y+1, len(nums)):
                if nums[x]+nums[y]+nums[z] not in sum_num:
                    sum_num.append(nums[x]+nums[y]+nums[z])
    sum_num.sort(reverse=True)
    print('#{} {}'.format(tc, sum_num[4]))
