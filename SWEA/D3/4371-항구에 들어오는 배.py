import sys
sys.stdin = open('항구.txt')
# tc = 3
# tc1 - N = 3 / 1 3 4
# tc2 - N = 5 / 1 7 10 13 19
# tc3 - N = 3 / 1 500000000 999999999

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    num = [int(input()) for _ in range(N)]  # 즐거운 날 목록

    result = 0
    while len(num) > 1:         # num리스트에 1만 남을때까지
        diff = num[1] - 1       # 1과의 차이    / 밑에서 check번호가 계속 삭제되니까 diff와 check는 계속 바뀐다.
        check = num[1]          # num[1]부터 시작
        while check <= max(num): # num[-1] 혹은 max(num), check가 제일 큰 값보다 커지면
            if check in num:     # num리스트에 check가 있다면
                num.remove(check)   # 리스트에서 삭제
            check += diff       # 차이만큼 더해주기
        result += 1

    print('#{} {}'.format(tc, result))
