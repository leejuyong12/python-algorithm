def check(date_time, aware_time):
    if aware_time == date_time:
        return 0
    elif aware_time > date_time:
        return aware_time - date_time
    else:
        return -1


TC = int(input())
for tc in range(1, TC + 1):
    D, H, M = map(int, input().split())  # 깨달음을 얻은 시간

    # 소개팅 약속 시간(기준 시간_
    date_time = 11 * 24 * 60 + 11 * 60 + 11

    aware_time = D * 24 * 60 + H * 60 + M

    print('#{} {}'.format(tc, check(date_time, aware_time)))