import sys
sys.stdin = open('의석이의 세로로 말해요.txt')

TC = int(input())
for tc in range(1, TC+1):
    text = [list(input()) for _ in range(5)]

    max_len = 0
    for x in text:
        if len(x) > max_len:
            max_len = len(x)
            
    res = ''
    for x in range(max_len):
        for y in range(len(text)):
            if len(text[y]) > x:
                res += text[y][x]
    print('#{} {}'.format(tc, res))

# T = int(input())
#
# for tc in range(1, T + 1):
#     # 테스트케이스는 총 다섯 줄
#     ARR = [list(input()) for _ in range(5)]
#     print(f'#{tc} ', end='')
#
#     for x in range(15):  # 행
#         for y in range(5):  # 열
#             try:
#                 print(ARR[y][x], end='')
#
#             except:
#                 print('', end='')
#     print()

