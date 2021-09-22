TC = int(input())

for tc in range(1, TC+1):
    S = list(input())
    new_S = set(S)
    base = []
    for x in range(len(S)):
        if S[x] in base:
            base.pop(base.index(S[x]))
        else:
            base.append(S[x])
    result = ''
    if len(base) == 0 and len(new_S) == 2:
        result = 'Yes'
    else:
        result = 'No'
    print('#{} {}'.format(tc, result))
