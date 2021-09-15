def check(lst):
    for x in range(len(a)):
        if a[x] == '{' or a[x] == '(':
            lst.append(a[x])
        elif a[x] == '}' or a[x] == ')':
            if len(lst) == 0:       # lst가 다 비워지면 종료!
                return 0

            p = lst.pop(-1)

            if a[x] == '}' and p != '{':    # 괄호 순서가 잘못되었는지 체크
                return 0
            elif a[x] == ')' and p != '(':
                return 0

    if len(lst) == 0:   # 남아있는지 없는지
        return 1
    else:
        return 0

TC = int(input())

for tc in range(1, TC+1):
    a = input()
    lst = []

    ans = check(lst)

    print('#{} {}'.format(tc, ans))
