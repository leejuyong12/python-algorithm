def solution(n):
    answer = ''
    fir = '수'
    sec = '박'
    while True:
        answer += fir
        n -= 1
        if n <= 0:
            break
        answer += sec
        n -= 1
        if n <= 0:
            break
    return answer