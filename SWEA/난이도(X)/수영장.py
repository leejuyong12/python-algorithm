import sys
sys.stdin = open('수영장.txt')

def cost_check(cost, m):
    global min_cost

    if m > 12:      # 12 넘어가면 이용권 끝
        if min_cost > cost:
            min_cost = cost
        return
    cost_check(cost + (day*plan[m]), m+1)   # 1일권
    cost_check(cost + month, m+1)           # 1달권
    cost_check(cost + month3, m+3)          # 3달권


TC = int(input())

for tc in range(1, TC+1):
    day, month, month3, year = map(int, input().split())

    plan = [0] + list(map(int, input().split()))
    min_cost = year  # 가장 큰 가격을 제일 비싼 연간 이용권으로 설정

    cost_check(0, 1)
    print('#{} {}'.format(tc, min_cost))
