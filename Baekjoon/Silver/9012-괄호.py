import sys
sys.stdin = open('괄호.txt')

N = int(input())
for n in range(N):
    lst = list(input())
    stack = []
    for x in lst:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break  # 이게 나온순간 일단 NO가 된다. 그래서 break한다.

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')