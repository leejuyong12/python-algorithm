n, m, t = map(int, input().split())

tow_ham = 0
bul_ham = 0
coke = 0

while t >= 0:
    if m >= n:
        if t % n == 0:
            tow_ham += t // n
            break
        else:
            t -= n
            tow_ham += 1
            t1 = t              # t1 임시로 설정

            # if t1 < n:          # 불고기 버거 추가
            #     while 0 < t1 <= t:
            #         t1 += n
            #         tow_ham -= 1
            #         t1 -= m
            #         bul_ham += 1
            #         if t1 == 0:
            #             coke = t1
            #             break

    if m < n:
        if t % m == 0:
            bul_ham += t // m
            break
        else:
            t -= m
            bul_ham += 1
            t1 = t
            if 0 < t1 < n:           # 타워버거 버거 추가
                while True:
                    t1 += m
                    bul_ham -= 1
                    t1 -= n
                    tow_ham += 1
                    if t1 == 0:
                        coke = t1
                        break
                    coke = t
                    break
print(bul_ham + tow_ham, coke)

#
# n, m, t = map(int, input().split())
#
#
# coke = 0
# result = []
# if m >= n:
#     for x in range(t // n, -1, -1):
#         for y in range(0, t //m):
#             if x * n + y * m == t:
#                 result.append(x + y)
#                 coke = 0
#                 break
#             # else:             # 딱 안나눠떨어진다면??
#             #     result.append(t // n)
#             #     coke = t - max(result) * n
#
# if n > m:
#     for x in range(t // m, -1, -1):
#         for y in range(0, t //n):
#             if x * m + y * n == t:
#                 result = x + y
#                 coke = 0
#                 break
#             else:
#                 result.append(t // m)
#                 coke = t - max(result) * m
# print(max(result), coke)