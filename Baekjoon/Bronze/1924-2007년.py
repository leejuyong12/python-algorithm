x, y = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum_day = 0
if x == 1:
    sum_day += y
else:
    for i in range(1, x+1):
        sum_day += days[i-1]  # 2 - days[1]   3 - days[2]
    sum_day += y

if sum_day % 7 == 1:
    print('MON')
elif sum_day % 7 == 2:
    print('TUE')
elif sum_day % 7 == 3:
    print('WED')
elif sum_day % 7 == 4:
    print('THU')
elif sum_day % 7 == 5:
    print('FRI')
elif sum_day % 7 == 6:
    print('SAT')
elif sum_day % 7 == 0:
    print('SUN')

# 다른사람 풀이
# Day = 0
# arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
#
# x, y = map(int,input().split())
#
# for i in range(x-1):
#     Day = Day + arrList[i]
# Day = (Day + y) % 7
#
# print(weekList[Day])