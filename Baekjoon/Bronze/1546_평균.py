# 정답에 확신이 없어서 다시 한번 봐보자.

N = int(input())

x = list(map(int, input().split()))  # 입력받은 값을 list로 정리.

M = max(x)  # 리스트에서 최댓값 구하기

avg_score = ((sum(x) / M)*100) / N  # 평균구하기

print(avg_score)  