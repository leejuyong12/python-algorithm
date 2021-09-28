N = int(input())

lst = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0

total += len(lst)       # 총감독관 수
lst_1 = []
for x in lst:           # 총감독관이 감독할 수 있는 인원 빼기
    if x > B:
        lst_1.append(x-B)
    elif x <= B:
        lst_1.append(0)

for y in lst_1:         # 부감독관 수 구하기
    if y == 0:          # 응시인원이 0이면 감독관이 필요없다
        total += 0
    elif y <= C:        # 응시인원이 한명의 부감독관이 감독할 수 있는 수보다 적다면
        total += 1      # 부 감독관 한명만 추가
    elif y > C:         # 응시인원이 한명의 부감독관이 감독할 수 있는 수보다 많다면
        if y % C == 0:  # 그 중에서 딱 나눠떨어진다면
            total += (y // C)   # 딱 그 몫만 더해준다
        else:
            total += (y // C) + 1   # 나머지가 있다면 남은 수에 대한 감독관 한명 추가
print(total)