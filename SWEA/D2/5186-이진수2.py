# # 내 풀이
# def ToBin(num):
#     global res, cnt, a
#     while num:              # num이 0이 되면 끝
#         if num < 2**-a:     # ex) num = 0.125   2**-a = 0.5
#             res += '0'      # 이러면 2**-a 를 쓸일이 없으니 0추가
#         else:               # ex) num 0.625    2**-a = 0.5
#             num -= 2**-a    # 이러면 0.5만큼 뺄 수 있으므로
#             res += '1'      #  1추가
#         cnt += 1            # 실행횟수만큼 cnt 추가
#         if cnt >= 13:        # 만약에 cnt가 13이상이면
#             return 'overflow'   # overflow 출력
#         else:                # 그 외에는
#             a += 1           # 1/2 1/4 1/8 계속 만들어가준다.
#     return res
#
#
# TC = int(input())
#
# for tc in range(1, TC+1):
#     N = float(input())
#
#     res = ''
#     cnt = 0
#     a = 1           # 1/2 부터 시작
#     print('#{} {}'.format(tc, ToBin(N)))

# 교수님 풀이
TC = int(input())

for tc in range(1, TC+1):
    N = float(input())
    C = 1

    res = ''
    found = False
    for i in range(12):
        C = C * 0.5
        if N == 0:
            found = True
            break
        if N >= C:
            N = N - C
            res += '1'
        else:
            res += '0'
    if found:
        print(res)
    else:
        print('overflow')