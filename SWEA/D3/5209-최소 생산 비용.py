import sys
sys.stdin = open('최소생산비용.txt')

def check(x, num_sum):
    global result

    # if result <= num_sum:
    #     return
    if x == N:
        if result > num_sum:
            result = num_sum
        return

    if result < num_sum:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            check(x+1, num_sum + arr[x][i])
            visited[i] = 0      # 1차원으로 만들었으니 방문했던거 다시 0으로 만들기(새로운 행으로 갈때마다)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 987654321
    check(0, 0)
    print('#{} {}'.format(tc, result))
