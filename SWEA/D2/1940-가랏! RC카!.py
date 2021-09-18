# 0은 현재 속도 유지,  1은 가속, 2는 감속

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    distance = 0    # 현재 온 거리
    velocity = 0    # 현재 속도
    for n in range(N):
        about = list(map(int, input().split()))
        if about[0] == 1:       # 가속
            velocity += about[1]
            distance += velocity
        elif about[0] == 2:     # 감속
            if velocity < about[1]:     # 만약에 현재속도보다 감속할 속도가 크면
                velocity = 0            # 속도는 0이 된다.
            else:
                velocity -= about[1]
                distance += velocity
        elif about[0] == 0:     # 유지
            distance += velocity
    print('#{} {}'.format(tc, distance))
