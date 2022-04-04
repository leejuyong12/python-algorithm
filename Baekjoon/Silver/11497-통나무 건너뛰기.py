import sys
sys.stdin = open('통나무 건너뛰기.txt')
# 규칙이 있다
# 13 10 12 11 10 11 12
# 1 2 3 4 5 -> 1 3 5 4 2
# 2 4 5 7 9 -> 2 5 9 7 4
# 2 34 77 88 92 100 -> 2 77 92 100 88 34
T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    max_ans = 0
    for x in range(N-2):
        max_ans = max(max_ans, abs(lst[x+2] - lst[x] ))
    print(max_ans)