import sys
sys.stdin = open('균형잡힌세상.txt')
from collections import deque
while True:
    lst = sys.stdin.readline().rstrip()
    if lst == '.':
        break
    stack = deque()
    for x in range(len(lst)):
        if lst[x] == '(' or lst[x] == '[':
            stack.append(lst[x])
        elif lst[x] == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(lst[x])
                break
        elif lst[x] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(lst[x])
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

