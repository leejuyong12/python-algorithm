def check(A, B):
    N = len(A)  # 긴 문자열
    M = len(B)  # 짦은 문자열

    cnt = 0
    i = 0
    while i < N - M + 1:
        j = 0
        while j < M and B[j] == A[i + j]:
            j += 1
        if j == M:
            cnt += 1
            i += j
        else:
            i += 1
    # 원래 했더 풀이가 안된이유는 bananana 에서 nana를 2번 찾아버린다.
    # 그래서 원래 10번에 for문을 썼었는데 while문으로 바꿨다. 그리고 cnt+=1 밑에 i += j 그리고 else: i+=1 추가해줌
    return cnt + N - (cnt * M)


TC = int(input())

for tc in range(1, TC + 1):
    A, B = input().split()

    ans = check(A, B)

    print('#{} {}'.format(tc, ans))