import sys
sys.stdin = open('Flatten.txt')

def max_P(lst):
    max_num = lst[0]
    max_idx = 0
    for x in range(1, len(lst)):
        if max_num < lst[x]:
            max_num = lst[x]
            max_idx = x
    return max_idx

def min_P(lst):
    min_num = lst[0]
    min_idx = 0

    for x in range(1, len(lst)):
        if min_num > lst[x]:
            min_num = lst[x]
            min_idx = x
    return min_idx

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))

    # for i in range(N):
    #     lst[max_P(lst)] -= 1
    #     lst[min_P(lst)] += 1
    #
    # final_max_num = lst[max_P(lst)]
    # final_min_num = lst[min_P(lst)]
    #
    # print('#{} {}'.format(tc, final_max_num-final_min_num))

    for i in range(N):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1

    final_max_num = lst[lst.index(max(lst))]
    final_min_num = lst[lst.index(min(lst))]

    print('#{} {}'.format(tc, final_max_num-final_min_num))