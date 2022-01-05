import sys
sys.stdin = open('괄호의 값.txt')

lst = list(input())
stack = []
answer = 0
tmp = 1
for x in range(len(lst)):
    if lst[x] == '(':
        stack.append(lst[x])
        tmp *= 2
    elif lst[x] == '[':
        stack.append(lst[x])
        tmp *= 3
    elif lst[x] == ')':
        if len(stack) == 0 or stack[-1] == '[':
            answer = 0
            break
        if lst[x-1] == '(':  # break 안쓰고 + elif 쓰면 런타임에러
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if len(stack) == 0 or stack[-1] == '(':
            answer = 0
            break
        if lst[x-1] == '[':  # stack[-1] 이 아니라 lst[x-1] 이다
            answer += tmp
        stack.pop()
        tmp //= 3
if len(stack) == 0:
    print(answer)
else:
    print(0)