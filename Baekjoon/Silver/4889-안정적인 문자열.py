import sys
sys.stdin = open('안정적인문자열.txt')
TC = 1

while True:
    cnt = 0

    lst = list(input())
    if '-' in lst:
        break
    check = []
    for x in lst:
        if x == '{':
            check.append(x)
        elif len(check) == 0 and x == '}': # } { 이런 짝이면 하나를 더 바꿔야 한다.
            cnt += 1
            check.append('{')
        elif len(check) != 0 and x == '}':
            check.pop()

    N = len(check) // 2         # check에 남은 건 {{ 나 }} 요런 느낌! 하나만 바꿔도 되는 것!
    print('{}. {}'.format(TC, N + cnt))
    TC += 1
