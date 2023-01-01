import sys
sys.stdin = open('1003-피보나치함수.txt')
# DP 문제(이전것을 활용하자!)
N = int(input())

cnt_0 = [1, 0, 1]
cnt_1 = [0, 1, 1]
def fibonacci(n):
    len_cnt = len(cnt_0)
    if len_cnt <= n:
        for i in range(len_cnt, n+1):
            cnt_0.append(cnt_0[i-1] + cnt_0[i-2])
            cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    print('{} {}'.format(cnt_0[n], cnt_1[n]))
for _ in range(N):
    x = int(input())
    fibonacci(x)


