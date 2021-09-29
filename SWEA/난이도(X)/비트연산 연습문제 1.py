# 2진수의 값을 10진수로 출력하기

lst = '0000001001101'

def binStrToDec(binStr):
    binStr = list(map(int, binStr))
    res = 0
    for i in range(len(binStr)):
        res = res*2 + binStr[i]
    return res

for pos in range(0, len(lst), 7):
    org = lst[pos:pos+7]
    print(binStrToDec(org))