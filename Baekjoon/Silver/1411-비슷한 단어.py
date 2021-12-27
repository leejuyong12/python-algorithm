import sys
sys.stdin = open('비슷한단어.txt')

# 조건 : 길이가 같은가? ->
N = int(input())
lst = [list(input()) for _ in range(N)]
cnt = 0
for x in range(N-1):
    for y in range(x+1, N):
        check = True
        if len(lst[x]) == len(lst[y]):
            visited1 = [0] * 26
            visited2 = [0] * 26
            for k in range(len(lst[x])):
                idx1 = ord(lst[x][k]) - ord('a')
                idx2 = ord(lst[y][k]) - ord('a')
                if visited1[idx1] == 0 and visited2[idx2] == 0:     # 짝이 없으면
                    visited1[idx1] = lst[y][k]                      # 짝 지어주기
                    visited2[idx2] = lst[x][k]
                elif visited1[idx1] != lst[y][k]:
                    check = False
                    break
        if check:
            cnt += 1
print(cnt)