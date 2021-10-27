T = int(input())

for x in range(T*2-1):
    if x <= (T*2-1) // 2:
        print('*' * (x+1))
    else:
        print('*' * ((T*2-1)-x))
