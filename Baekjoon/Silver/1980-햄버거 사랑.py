n, m, t = map(int, input().split())

eat_tow = 0
eat_ham = 0
result = []
while eat_tow >= 0:

    if t-(eat_tow*n)-(eat_ham*m) <= 0:
        result.append(0)
        eat_tow -= 1
        eat_ham += 1
    else:
        result.append(t-(eat_tow*n)-(eat_ham*m))
        eat_tow -= 1
        eat_ham += 1
print(result)
print(eat_tow+eat_ham)
