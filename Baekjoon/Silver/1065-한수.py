import sys
sys.stdin = open('1065-백준-한수.txt')

TC = 4
for tc in range(1, TC+1):
    num = int(input())

    cnt = 0
    for x in range(1, num+1):
        if len(str(x)) == 1:
            cnt += 1
        elif len(str(x)) == 2:
            cnt += 1
        elif len(str(x)) == 3:
            if (x // 100) >= (x - (x//100)*100)//10 and (x - (x//100)*100)//10 >= x % 10:
                if ( (x // 100) - (x - (x//100)*100)//10 ) == ( (x - (x//100)*100)//10 - x % 10):
                    cnt += 1
            elif (x // 100) <= (x - (x//100)*100)//10 and (x - (x//100)*100)//10 <= x % 10:
                if ( (x // 100) - (x - (x//100)*100)//10 ) == ( (x - (x//100)*100)//10 - x % 10):
                    cnt += 1
    print(cnt)