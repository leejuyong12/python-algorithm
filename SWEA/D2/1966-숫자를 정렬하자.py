TC = int(input())

for tc in range(1, TC+1):
    N = int(input())

    nums = list(map(int, input().split()))
    nums.sort()
    result = ''
    for x in nums:
        result += str(x) + ' '
    print('#{} {}'.format(tc, result))
