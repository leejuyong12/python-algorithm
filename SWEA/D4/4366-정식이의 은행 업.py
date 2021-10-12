import sys
sys.stdin = open('정식이.txt')

def change_to_dec(num, notation):
    tmp = 0

    for n, val in enumerate(list(map(int, num))[::-1]):     # n은 index val는 index에 위치한 값
        tmp += val * (notation**n)
    return tmp


# enumerate 사용안할 때
def change_to_dec2(num, notation):
    tmp = 0
    n = len(num)-1
    for i in num:
        tmp += i * (notation**n)
        n -= 1
    return tmp

def check(num, notation):
    change_num = change_to_dec(num, notation)   # 10진수 값을 저장
    #change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j:
                continue
            tmp = change_num - val * (notation**n) + j * (notation ** n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp
TC = int(input())
for tc in range(1, TC+1):
    N2 = input()
    N3 = input()

    binary = []
    check(N2, 2)
    print('#{} {}'.format(tc, check(N3, 3)))