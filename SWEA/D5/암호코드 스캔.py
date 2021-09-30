import sys
sys.stdin = open('암호코드 스캔.txt', 'r')

h2b = {'0':'0000',
       '1':'0001',
       '2':'0010',
       '3':'0011',
       '4':'0100',
       '5':'0101',
       '6':'0110',
       '7':'0111',
       '8':'1000',
       '9':'1001',
       'A':'1010',
       'B':'1011',
       'C':'1100',
       'D':'1101',
       'E':'1110',
       'F':'1111'

       }

pwd = {112:0,
       221:1,
       122:2,
       411:3,

       }

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    arrh = [input() for _ in range(N)]

    for j in range(M):
        arrb[i] += h2b[arrh[i][j]]  # 16진수 -> 비트 패턴
    M *= 4

    arrb = [''] * N
    for i in range(N):
        j = M-1
        while arrb[i][j] == '0':        # '1'을 만날때까지 이동
            j -= 1
        c1 = 0
        while arrb[i][j] == '1':
            c1 += 1
            j -= 1
        c2 = 0
        while arrb[i][j] == '0':
            c2 += 1
            j -= 1
        c3 = 0
        while arrb[i][j] == '1':
            c3 += 1
            j -= 1

        num[k] = pwd[c3 * 100 + c2 * 10 + c1]
        k += 1


    # for i in range(N):
    #     c1 = 0
    #     c2 = 0
    #     c3 = 0
    #     for j in range(M-1, 54, -1):
    #         if c1 == 0 and arrb[i][j] == '1':   # 0110011  <-
    #             c1 += 1
    #         elif c != 0arrb[i][j] == '0'

