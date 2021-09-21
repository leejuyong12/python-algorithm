A, B, V = map(int, input().split())

day = 0
if (V-B) % (A-B) == 0:      # (V-B) % (A-B)  도착했을때 안미끄러지니까 (V-B) 지금은 그냥 (A-B)*날짜 개념으로 푼다고 이해하자 그래서 A-B를 분모로 놔두자
    day = (V-B) // (A-B)    # 그니깐 딱 나눠 떨어지면 1 더해줄 필요가 없다
else:
    day = (V-B) // (A-B) + 1
print(day)
# while True:
#     day += 1
#     if A*day-B*(day-1) >= V:
#         break
# print(day)

# while True:
#     height += A
#     day += 1
#     if height >= V:
#         break
#     height -= B
# print(day)