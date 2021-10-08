import sys
sys.stdin = open('격자판.txt')
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def check(nums, x, y):

    if len(nums) == 7:
        result.add(nums) # 서로 다른 값 넣기
        return
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < 4 and 0 <= new_x < 4:  # 범위 내에서
            check(nums+arr[new_y][new_x], new_x, new_y)

TC = int(input())

for tc in range(1, TC+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            check(arr[i][j], j, i)
    print('#{} {}'.format(tc, len(result)))