year_1 = int(input())

if year_1 % 4 == 0 and (year_1 % 100 != 0 or year_1 % 400 == 0):
    print(1)
else:
    print(0)