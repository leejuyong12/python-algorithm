import sys
sys.stdin = open('배수 스위치.txt')

TC = int(input())
for tc in range(1, TC+1):
    text = ['N'] + list(input())        # Y는 켜진 상태, N은 꺼진 상태
                                # 모두다 꺼야 한다.
    base = ['N'] * len(text)
    cnt = 0
    for x in range(1, len(text)):
        if text[x] != base[x]:
            for y in range(x, len(text), x):
                if text[y] == 'Y':
                    text[y] = 'N'
                elif text[y] == 'N':
                    text[y] = 'Y'
            cnt += 1
    for z in range(len(text)):
        if z == 'Y':
            print(-1)
    print(cnt)