TC = int(input())

for tc in range(1, TC+1):
    text = input()

    for i in range(1, 10):
        if text[:i] == text[i:i*2]:
            print('#{} {}'.format(tc, i))
            break
# SAMSUNG 의 예제 분석
# i = 1     S           A
# i = 2     SA          MS
# i = 3     SAM         SUN
# i = 4     SAMS        UNGS
# i = 5     SAMSU       NGSAM
# i = 6     SAMSUN      GSAMSU
# i = 7     SAMSUNG     SAMSUNG
