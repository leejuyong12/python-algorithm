n, m, t = map(int, input().split())

coke = 0
total = 0
tmp_t = t

while True:
    if tmp_t == 0:
        break

    if tmp_t < 0:           # 시간 오래 걸리는걸 빼다보면 tmp_t가 음수가 나오는 경우가 있다(7, 9, 26)
        coke += 1           # 콜라 추가
        tmp_t = t - coke    # 콜라 마신 만큼 시간에서 빼준다.(콜라먹는 시간을 1분으로 생각)
        total = 0           # 콜라를 뺀만큼부터 햄버거 다시 계산해주기

    if n <= m:
        if tmp_t % n == 0:
            total += tmp_t // n
            tmp_t = 0

        elif tmp_t % n != 0:
            tmp_t -= m      # 어차피 n으로 나누어떨어지지 않는다면 m은 무조건 포함해야한다.(콜라를 최소로 하기 위해)
            total += 1

    elif n > m:
        if tmp_t % m == 0:
            total += tmp_t // m
            tmp_t = 0

        elif tmp_t % m != 0:
            tmp_t -= n      # 어차피 m으로 나누어떨어지지 않는다면 n은 무조건 포함해야한다.(콜라를 최소로 하기 위해)
            total += 1

print('{} {}'.format(total, coke))