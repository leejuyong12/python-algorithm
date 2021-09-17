TEXT = list(input())

base = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for x in range(len(base)):
    for y in range(len(base[x])):
        for z in range(len(TEXT)):
            if base[x][y] == TEXT[z]:
                cnt += x
print(cnt)