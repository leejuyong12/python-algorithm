# 10진수의 값을 2진수로 출력하기
# 10 => 00001010

def dectobin(num):
    res = ''
    for j in range(7, -1, -1):
        # j bit
        if num & (1 << j):
            res += '1'
        else:
            res += '0'
    return res

print(dectobin(10))