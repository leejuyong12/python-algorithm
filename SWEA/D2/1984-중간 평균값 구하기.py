TC = int(input())

for tc in range(1, TC + 1):
    nums = list(map(int, input().split()))

    max_num = max(nums)
    min_num = min(nums)

    sum_num = 0
    length_num = len(nums) - 2
    for num in nums:
        if num != max_num and num != min_num:
            sum_num += num

    avg_num = round(sum_num / length_num)

    print('#{} {}'.format(tc, avg_num))