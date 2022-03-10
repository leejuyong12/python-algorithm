def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    text = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = 0
    for x in range(1, a):
        day += days[x]
    day += b
    plus = day % 7
    ans = text[plus]
    return ans