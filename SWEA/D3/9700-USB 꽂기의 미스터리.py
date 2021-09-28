TC = int(input())

for tc in range(1, TC+1):
    p, q = map(float, input().split())

    s1 = (1-p) * q  # (1-p)잘못된 면 (q)정상적으로 꽂는 것
    s2 = p * (1-q) * q  # (p) 올바른 면 (1-q)비정상적으로 꽂고 (q)정상적으로 꽂음

    if s1 < s2:
        result = 'YES'
    else:
        result = 'NO'

    print('#{} {}'.format(tc, result))