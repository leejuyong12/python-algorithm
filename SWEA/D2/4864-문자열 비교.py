def check(str1, str2):

    N = len(str1)
    M = len(str2)

    for i in range(M-N+1):
        j = 0
        while j < N and str1[j] == str2[i+j]:
            j += 1
        if j == N:
            return 1
    else:
        return 0

TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    ans = check(str1, str2)

    print('#{} {}'.format(tc, ans))