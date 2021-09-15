TC = int(input())

for tc in range(1, TC + 1):
    arr = input()
    st = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            st.append(arr[i])
        elif arr[i] == ')':
            st.pop(-1)
            if arr[i - 1] == '(':
                cnt += len(st)  # 그 전꺼 누적
            elif arr[i - 1] == ')':
                cnt += 1  # 막대기 하나가 끝났다 (다음번에 처리 안해주려고)
    print('#{} {}'.format(tc, cnt))