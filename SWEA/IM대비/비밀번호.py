import sys
sys.stdin = open('비밀번호.txt')

TC = 10
for tc in range(1, TC+1):
    N, password = input().split()

    new = [password[0]]
    for x in range(1, int(N)):
        if len(new) > 0 and new[-1] == password[x]:
            new.pop(-1)
        else:
            new.append(password[x])
    res = ''
    for i in range(len(new)):
        res += new[i]
    print('#{} {}'.format(tc, res))
