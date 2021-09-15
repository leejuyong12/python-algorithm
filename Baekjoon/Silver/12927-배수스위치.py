import sys
sys.stdin = open('12927-배수스위치-백준.txt')

TC = 4
for tc in range(1, TC+1):

    lights = ['N'] + list(map(str, input()))        # Y는 켜져있을때, N은 꺼져있을때
    base = ['N'] * len(lights)

    cnt = 0
    for x in range(1, len(lights)):
        if lights[x] != base[x]:
            for y in range(x, len(lights), x):
                if lights[y] == 'Y':
                    lights[y] = 'N'
                elif lights[y] == 'N':
                    lights[y] = 'Y'
            cnt += 1

    for z in lights:
        if z == 'Y':
            cnt = -1

    print(cnt)
