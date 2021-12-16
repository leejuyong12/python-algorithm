import sys
sys.stdin = open('30.txt')
# 아이디어 참고
N = list(input())
res = ''
if '0' not in N:        # 30이니까 무조건 1의 자리에는 0이 와야 한다.
    print(-1)
else:
    for x in range(len(N)):
        res += N[x]
    if int(res) % 3 != 0:   # 30의 배수가 되어야 하니까 3의 배수도 되어야 한다.
        print(-1)
    else:
        N.sort(reverse=True)    # 각 자리의 합이 3의 배수이면 그 수는 3의 배수이다.(초딩수학)
        for x in range(len(N)):
            print(N[x], end='')