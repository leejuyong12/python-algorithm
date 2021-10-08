import sys
sys.stdin = open('퀵 정렬.txt')

def quick_sort(lst, l, r):
    if l < r:
        s = partitionH(l, r)
        quick_sort(lst, l, s-1) # 피봇 기준 왼쪽
        quick_sort(lst, s+1, r) # 피봇 기준 오른쪽

def partitionH(l, r):
    p = l
    i = l       # l+1
    j = r

    while i < j:    # 이때 동안 밑에거를 다 돌려라

        while i < r and lst[i] <= lst[p]:
            i += 1

        while j > l and lst[j] >= lst[p]:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]


    # 위의 while 문 끝나면 i j 역전된 상태
    lst[p], lst[j] = lst[j], lst[p]
    return j

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick_sort(lst, 0, N-1)

    print('#{} {}'.format(tc, lst[N//2]))
