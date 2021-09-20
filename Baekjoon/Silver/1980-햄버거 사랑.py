n, m, t = map(int, input().split())

tow = 0
bul = 0
coke = 0
t_1 = t

if n > t and m > t:     # 타워버거와 불고기버거를 먹는 시간이 주어진 시간보다 크면 그 시간에 콜라를 마신다.
    coke = t
if n <= t and m > t:   # 타워버거만 t보다 작을 때
    while True:
        tow += 1
        t = t - n
        if t < n:
            coke = t
            break
if n > t and m <= t:    # 불고기버거만 t보다 작을 때
    while True:
        bul += 1
        t = t - m
        if t < m:
            coke = t
            break
if n <= t and m <= t:   # 타워버거와 불고기 버거가 모두 t보다 작을 때
    while True:
        if n >= m:
            bul += 1
            t = t - m
            if 0 < t < :


        if n <= m:
            tow += 1
            t = t - n
            if t < m:
                if t_1 == bul * m + tow * n:
                    break
                t = t + n
                tow -= 1
                t = t - m
                bul += 1
            coke = t
print(tow, bul, coke)

