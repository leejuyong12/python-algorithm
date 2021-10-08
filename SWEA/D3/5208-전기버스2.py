import sys
sys.stdin = open('전기버스2.txt')

def solve(k, remain, cnt):
    global minC                             # if문 순서 중요
    if minC <= cnt:      # 백트래킹     # 이전에 나온 값보다 더 큰 경우를 사전에 차단
        return

    if k == lst[0]:
        if minC > cnt:
            minC = cnt
        return                  # 여기에 return 이 있는 이유는 저 if문 충족한거를 다 보기 위해

    if remain == 0:             # 못가는 경우        # 배터리가 없어서 못갈 때
        return

    solve(k+1, lst[k+1], cnt+1) # 충전 한 경우
    solve(k+1, remain-1, cnt)     # 충전 안한경우


TC = int(input())

for tc in range(1, TC+1):
    lst = list(map(int, input().split())) + [0]     # [0] 안넣으면 list index 오류
    minC = 100
    solve(1, lst[1], 0)
    print('#{} {}'.format(tc, minC))