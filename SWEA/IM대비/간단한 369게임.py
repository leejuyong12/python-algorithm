N = int(input())

for n in range(1, N+1):
    cnt = 0
    for x in list(str(n)):
        if x in ['3', '6', '9']:
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end = ' ')
    else:
        print(n, end = ' ')