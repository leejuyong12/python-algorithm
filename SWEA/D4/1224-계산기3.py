def step1(s):
    isp = {'(': 0, '+': 1, '*': 2}
    icp = {'+': 1, '*': 2, '(': 3}  # 숫자가 작을수록 순서가 빠르다
    t = []
    ST = []  # 연산자스택

    for c in s:
        if c.isdecimal():  # 숫자면 t에 넣어
            t.append(c)
        # 여기서부터는 연산자일 경우
        elif c == ')':  # )가 나오면
            while ST[-1] != '(':  # (가 나올때까지 연산자를 pop해서 t에 넣어주자
                t.append(ST.pop())
            ST.pop()  # 위의 경우 말고는 ST의 연산자 pop하기
        else:
            if len(ST) == 0 or isp[ST[-1]] < icp[c]:  # ST에 아무것도 없거나 새로 들어오는 연산자의 순서가 더 빠르면 그냥 그대로 넣어라
                ST.append(c)
            else:
                while ST and isp[ST[-1]] >= icp[c]:  # 원래 있고 그것의 순서가 더 빠르거나 같으면 기존의 것(새로 들어오는 거보다 순서빠른거) 빼주고 넣어라
                    t.append(ST.pop())
                ST.append(c)  # 그게 아니면 그냥 ST에 연산자 넣어라
    while ST:  # 이제 남은 연산자들 차례로 t에 넣어주기
        t.append(ST.pop(-1))
    return t


def step2(t):  # 계산하기
    ST = []  # ST 빈공간 생성
    for c in t:
        if c.isdecimal():  # 숫자가 나오면 일단 ST에 넣기
            ST.append(int(c))
        else:
            x = int(ST.pop())  # 숫자 빼내서 처리해주고
            y = int(ST.pop())
            if c == '+':
                ST.append(x + y)  # 더한거 다시 넣기
            if c == '*':
                ST.append(x * y)  # 곱한거 다시 넣기
    return ST.pop()  # ST에 남은 값 꺼내기(최종 결과값)


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    cal = input()

    print('#{} {}'.format(tc, step2(step1(cal))))