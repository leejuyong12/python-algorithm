import sys
sys.stdin = open('삼성시의 버스 노선.txt')

# 시간초과

# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     tmp = []
#     for n in range(N):
#         A, B = map(int, input().split())
#         for x in range(A, B+1):
#             tmp.append(x)
#     P = int(input())
#     for p in range(P):
#         C = int(input())
#
#     counting = [0] * (P+1)
#     for y in range(len(tmp)):
#         counting[tmp[y]] += 1
#     res = ''
#     for z in range(1, len(counting)):
#         res += str(counting[z]) + ' '
#     print('#{} {}'.format(tc, res))

def bus_count(station_num):
    cnt = 0
    for i in range(N):
        if route[i][0] <= station_num <= route[i][1]:
            cnt += 1
    return cnt
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    route = []
    for n in range(N):
        A, B = map(int, input().split())
        route.append((A,B))
    P = int(input())
    res = []
    for p in range(P):
        C = int(input())
        res.append(bus_count(C))
    print('#{} {}'.format(tc, ' '.join(map(str, res))))

