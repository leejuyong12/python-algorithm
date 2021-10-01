import sys
sys.stdin = open('aaa.txt')

TC = int(input())

for tc in range(1, TC+1):
    A, B = map(int, input().split())


    num_1 = list(map(int, input().split()))
    num_2 = list(map(int, input().split()))

    if A > B:
        max_result = 0
        for x in range(A-B+1):
            result = 0
            for y in range(B):
                result += num_1[x+y] * num_2[y]
            if result > max_result:
                max_result = result

    elif A < B:
        max_result = 0
        for x in range(B-A+1):
            result = 0
            for y in range(A):
                result += num_2[x+y] * num_1[y]
            if result > max_result:
                max_result = result
    else:
        max_result = 0
        for x in range(A):
            max_result = num_1[x] * num_2[x]
    print('#{} {}'.format(tc, max_result))



