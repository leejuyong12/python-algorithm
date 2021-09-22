TC = int(input())

for tc in range(1, TC+1):
    text = list(input())

    a = 1
    b = 1
    for x in range(len(text)):
        if text[x] == 'L':
            b += a
        elif text[x] == 'R':
            a += b
    print('#{} {} {}'.format(tc, a, b))

# 다른 풀이

# for test_case in range(1, int(input()) + 1):
#     a, b = 1, 1
#     for w in input():
#         if w == "L":
#             a, b = a, a + b
#         else:
#             a, b = a + b, b
#
#     print("#{} {} {}".format(test_case, a, b))