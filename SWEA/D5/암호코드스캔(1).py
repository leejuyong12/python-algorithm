# patt = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001'
#        '0101111', '0111011', '0110111', '0001011']

import sys
sys.stdin = open('암호코드 스캔.txt')

pat = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

def hexToBinStr(arr):
    arr = arr.replace('0', '0000')
    arr = arr.replace('1', '0001')
    arr = arr.replace('2', '0010')
    arr = arr.replace('3', '0011')
    arr = arr.replace('4', '0100')
    arr = arr.replace('5', '0101')
    arr = arr.replace('6', '0110')
    arr = arr.replace('7', '0111')
    arr = arr.replace('8', '1000')
    arr = arr.replace('9', '1001')
    arr = arr.replace('A', '1010')
    arr = arr.replace('B', '1011')
    arr = arr.replace('C', '1100') # 12
    arr = arr.replace('D', '1101')
    arr = arr.replace('E', '1110')
    arr = arr.replace('F', '1111')


    return arr


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    ARR = [input() for _ in range(N)]
    for i in range(N):
        ARR[i] = hexToBinStr(ARR[i])


    sumV = 0

    for row in range(1, N):     # 주변에 0이 있으니까 1부터 시작
        if ARR[row].find('1') < 0:
            continue

        col = M * 4 - 1
        while col > 56:
            if ARR[row][col] == '1' and ARR[row-1][col] == '0' :

                res = []
                for i in range(8):
                    cnt1 = cnt2 = cnt3 = 0
                    while ARR[row][col] == '1':
                        cnt1 += 1
                        col -= 1
                    while ARR[row][col] == '0':
                        cnt2 += 1
                        col -= 1
                    while ARR[row][col] == '1':
                        cnt3 += 1
                        col -= 1
                    while col >= 0 and ARR[row][col] == '0':
                        col -= 1

                    ratio = min(cnt1, cnt2, cnt3)
                    res.insert(0, pat.index(cnt3//ratio * 100 + cnt2//ratio * 10 + cnt1//ratio * 1))

                oddV = res[0] + res[2] + res[4] + res[6]
                evenV = res[1] + res[3] + res[5] + res[7]

                if ( oddV * 3 + evenV ) % 10 == 0:
                    sumV += sum(res)
            else:
                col -= 1

    print('#{} {}'.format(tc, sumV))