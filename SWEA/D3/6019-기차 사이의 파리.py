TC = int(input())

for tc in range(1, TC+1):
    D, A, B, F = map(int, input().split())

    fly_time = D / (A + B)      # 기차A 와 기차B가 서로 맞닿을때까지의 시간
    fly_distance = fly_time * F # 그 사이에서 파리는 계속 움직이므로 맞닿을때까지의 시간 * 파리의 속도

    print('#{} {}'.format(tc, fly_distance))