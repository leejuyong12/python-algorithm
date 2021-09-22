TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    nums = list(map(int, input().split()))
    cnt = 0
    for x in range(1, N-1):
        if nums[x] != max(nums[x-1], nums[x], nums[x+1]) and nums[x] != min(nums[x-1], nums[x], nums[x+1]):
            cnt += 1
    print('#{} {}'.format(tc, cnt))
# TC = int(input())
#
# for tc in range(1, TC+1):
#     N = int(input())
#
#     nums = list(map(int, input().split()))
#     max_num = max(nums)
#     min_num = min(nums)
#     cnt = 0
#     for x in range(len(nums)-2):
#         lst = []
#         for y in range(x, x+3):
#             lst.append(nums[y])
#         if lst[1] == max_num:
#             cnt += 0
#         elif lst[1] == min_num:
#             cnt += 0
#         elif lst[1] != max_num and lst[1] != min_num:
#             cnt += 1
#
#     print('#{} {}'.format(tc, cnt))