import sys
sys.stdin = open('Flatten.txt')

def find_max(lst):
    max_num = lst[0]
    max_id = 0
    for x in range(1, len(lst)):
        if max_num < lst[x]:
            max_num = lst[x]
            max_id = x
    return max_id

def find_min(lst):
    min_num = lst[0]
    min_id = 0
    for x in range(1, len(lst)):
        if min_num > lst[x]:
            min_num = lst[x]
            min_id = x
    return min_id


TC = 10
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))

    for x in range(N):
        lst[find_max(lst)] -= 1
        lst[find_min(lst)] += 1

        if max(lst) - min(lst) == 1 or 0:
            break
    print('#{} {}'.format(tc, max(lst)-min(lst)))