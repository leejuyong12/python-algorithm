def solution(dartResult):
    stack = []
    ans = 0
    for x in range(len(dartResult)):
        if dartResult[x] == 'D':
            if dartResult[x - 2] == '1':
                stack.append(10 ** 2)
            else:
                stack.append(int(dartResult[x - 1]) ** 2)


        elif dartResult[x] == 'S':
            if dartResult[x - 2] == '1':
                stack.append(10)
            else:
                stack.append(int(dartResult[x - 1]))
        elif dartResult[x] == 'T':
            if dartResult[x - 2] == '1':
                stack.append(10 ** 3)
            else:
                stack.append(int(dartResult[x - 1]) ** 3)
        elif dartResult[x] == '#':
            stack[-1] *= -1
        elif dartResult[x] == '*':
            if len(stack) >= 2:
                stack[-1] *= 2
                stack[-2] *= 2
            else:
                stack[-1] *= 2
    return sum(stack)