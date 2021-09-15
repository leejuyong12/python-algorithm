# 더 간단하게 하는 방법이 있는데 내 머리로는 아직 안된다..

T = int(input())

for a in range(T):
    x = input()
    year = str(x[0:4])
    month = str(x[4:6])
    day = str(x[6:8])    # 여기서 str로 만들고 나중에 비교할때 int로 만들어주기! 
                         # str에서 int로 바꾸기는 되는데 int에서 str로는 못바꾸는 거 기억하기!!

    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
        if int(day) > 31 or int(day) < 1:
            print(f'#{a+1} -1')
        else:
              print(f'#{a+1} {year}/{month}/{day}')
    elif month == '04' or month == '06' or month == '09' or month == '11':
        if int(day) > 30 or int(day) < 1:
            print(f'#{a+1} -1')
        else:
              print(f'#{a+1} {year}/{month}/{day}')
    elif month == '02':
        if int(day) > 28 or int(day) < 1:
            print(f'#{a+1} -1')
        else:
              print(f'#{a+1} {year}/{month}/{day}')              
    else:
        print(f'#{a+1} -1')