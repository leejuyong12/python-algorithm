# 인덱싱이랑 슬라이싱은 문자열에서만 가능
# N값을 받을때 str을 통해 문자열로 바꿔주고
# total 에 더해줄때 숫자로 활용하기 위해 다시 int로 바꿔준다.

N = str(input())

total = 0
for a in range(len(N)):
    total += int(N[a])
print(total)