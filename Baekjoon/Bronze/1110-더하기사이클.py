import sys
sys.stdin = open('1110-백준-더하기사이클.txt')
# 아이디어는 구글링 참고, 나머지랑 몫으로 구한다는 걸 일찍 알아차렸으면 금방 구했을 것이다!
TC = 4
for tc in range(1, TC+1):
    num = int(input())

    mid_num = num // 10 + num % 10
    new_num = mid_num % 10 + (num % 10) * 10

    cnt = 1
    while new_num != num:
        mid_num = new_num // 10 + new_num % 10
        new_num = mid_num % 10 + (new_num % 10) * 10
        cnt += 1
    print(cnt)
