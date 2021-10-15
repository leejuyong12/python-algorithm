import sys
sys.stdin = open('쇠막대기 자르기.txt')

# 직접 그리면서 이해하기

TC = int(input())
for tc in range(1, TC+1):
    iron = list(input())

    st = []
    cnt = 0
    for x in range(len(iron)):
        if iron[x] == '(':
            st.append(iron[x])

        elif iron[x] == ')':
            st.pop(-1)
            if iron[x-1] == '(':
                cnt += len(st)
            elif iron[x-1] == ')':
                cnt += 1
    print('#{} {}'.format(tc, cnt))