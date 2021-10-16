import sys
sys.stdin = open('가장 빠른 문자열 타이핑.txt')

def check(text, base):
    N = len(text)
    M = len(base)

    cnt = 0
    i = 0
    while i < N-M+1:                # 기본 시작점 i는 base길이 만큼 뺀 곳 까지 갈 수 있음
        j = 0
        while j < M and text[i+j] == base[j]:   # j는 base길이 비교를 위해 사용
            j += 1
        if j >= M:
            cnt += 1
            i += j
        else:
            i += 1

    return cnt + N - (cnt * M)
TC = int(input())
for tc in range(1, TC+1):
    text, base = input().split()

    print('#{} {}'.format(tc, check(text, base)))