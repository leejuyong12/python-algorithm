def max_num1(lst):
    m_num = 0
    for num in lst:
        if num > m_num:
            m_num = num
    return m_num


for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0

    max_num = lst[0]
    for i in range(2, N - 2):
        if lst[i] > max_num1([lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2]]):
            result += lst[i] - max_num1([lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2]])

    print('#{} {}'.format(tc, result))