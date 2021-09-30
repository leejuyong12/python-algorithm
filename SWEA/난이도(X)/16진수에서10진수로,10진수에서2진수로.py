# 16진수 -> 10진수

def HexToDec(num):
    if num.isdigit():
        numV = int(num)
    else:
        numV = ord(num) - ord('A') + 10
    return numV


# 10진수 -> 2진수
def DecToBin(num):
    res = ''
    for i in range(3, -1, -1):
        if num & (1 << i):
            res += '1'
        else:
            res += '0'
    return res

TC = int(input())

for tc in range(1, TC+1):
    N, N_16 = map(str, input().split())

    result = ''
    for x in N_16:
        result += DecToBin(HexToDec(x))

    print('#{} {}'.format(tc, result))



