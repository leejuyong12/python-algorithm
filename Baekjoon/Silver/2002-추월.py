import sys
sys.stdin = open('추월.txt')

N = int(input())
start = dict()
end = []
for i in range(N):
    s_car = input()
    start[s_car] = i    # 들어갈때 차명이랑 순서를 저장
for _ in range(N):
    e_car = input()
    end.append(e_car)   # 나오는 순서 저장
ans = 0                 # 나오는 순서(숫자)가 나올 수록 빨리 나온거
for i in range(N-1):
    for j in range(i+1, N):
        if start[end[i]] > start[end[j]]: # 들어갈때 순서와 나올때 순서 비교
            ans += 1
            break
print(ans)