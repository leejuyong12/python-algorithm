import sys
sys.stdin = open('스택.txt')

N = int(sys.stdin.readline())
stack = []
for x in range(N):
    program = sys.stdin.readline().split()      # 입력 받는거 이거로 해야 pass
    if program[0] == 'push':
        stack.append(program[1])
    elif program[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())  # pop(-1)했을때는 런타임에러 였는데 ()로 바꾸니까 pass

    elif program[0] == 'size':
        print(len(stack))
    elif program[0] == 'empty':
        if len(stack) == 0:
            print(1)
        elif len(stack) >= 1:
            print(0)
    elif program[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
