# 16진수의 값을 10진수로 출력하기

def binStrtoDec(binStr):
    binStr = list(map(int, binStr))
    res = 0
    for i in range(len(binStr)):
        res = res*2 + binStr[i]
    return res

# '0' => '0000', '9' => '1001', 'A' => '1010' , 'F' => '1111'
def hexToBinStr(hexV):

    if hexV.isdigit():
        numV = int(hexV)
    else:
        numV = ord(hexV) - ord('A') + 10

    tmp_res = ''
    for j in range(3, -1, -1):
        if numV & 1<<j:
            tmp_res += '1'
        else:
            tmp_res += '0'

    return tmp_res

lst = '0F97A3'
res = ''
for i in range(0, len(lst)):
    res += hexToBinStr(lst[i])

for pos in range(0, len(res), 7):
    org = res[pos:pos+7]
    print(binStrtoDec(org))