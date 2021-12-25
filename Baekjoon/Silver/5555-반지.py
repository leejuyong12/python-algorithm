import sys
sys.stdin = open('반지.txt')

ring = input()
N = int(input())
cnt = 0
for _ in range(N):
    rings = input()
    if ring in rings*2:     # 나는 반대로 돌아가는 탐색 생각했는데 구현이 쉽지 않아서
        cnt += 1            # 그냥 뒤에 그대로 붙여주는 방식이
print(cnt)

