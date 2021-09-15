# 테스트 케이스 분석
# 1이상 3이하에 들어가는건 C1, C2, C3 3개이다.   그래서 1 1 1이고
# 2이상 5이하에 들어가는건 C2, C3, C4, C5 4개이다. 그래서 1 1 1 1 씩 더하면  1 2 2 1 1 이 나온다.

def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if route[i][0] <= bus_stop <= route[i][1]:  # A이상 B이하에 들어가면 cnt +1 해주기
            cnt += 1
    return cnt


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    route = []

    for n in range(N):
        A, B = map(int, input().split())  # A이상 B이하의 정류장 다 지난다.
        route.append((A, B))
    P = int(input())
    ans = []

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))  # join 함수 기억!!