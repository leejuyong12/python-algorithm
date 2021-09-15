TC = 10

for tc in range(1, TC + 1):
    l = int(input())
    cal = input()

    t = []
    ST = ''

    for c in cal:
        if c == '+':
            while t:
                ST += t.pop()
            t.append(c)

        elif c == '*':
            if (not t) or t[-1] != '*':
                t.append(c)
            else:
                ST += c
        else:
            ST += c

    ST += t.pop()

    result = []
    for y in ST:
        if y == '+':
            result.append(result.pop() + result.pop())
        elif y == '*':
            result.append(result.pop() * result.pop())
        else:
            result.append(int(y))

    sum_result = 0
    for x in result:
        sum_result += x
    print('#{} {}'.format(tc, sum_result))