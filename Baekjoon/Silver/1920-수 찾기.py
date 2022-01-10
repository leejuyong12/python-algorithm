import sys
sys.stdin = open('수찾기.txt')

N = int(input())
lst_N = sorted(list(map(int, input().split())))
M = int(input())
lst_M = list(map(int, input().split()))

# 1 2 3 4 5
# 1 3 7 9 5
def binary(target):
    start = 0
    end = N-1
    # 범위 좁혀나가면서 찾기
    while start <= end:
        mid = (start + end) // 2
        if lst_N[mid] == target:
            return True
        if lst_N[mid] > target:
            end = mid - 1       # 찾아야 할 것이 중간값보다 -1을 end값으로 지정
        elif lst_N[mid] < target:
            start = mid + 1
for x in range(len(lst_M)):
    if binary(lst_M[x]):
        print(1)
    else:
        print(0)
