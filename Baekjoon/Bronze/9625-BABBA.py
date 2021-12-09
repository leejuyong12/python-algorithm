# K = int(input())
# # tmp_k = 0
# # start = ['A']
# # while tmp_k < K:
# #     for x in range(len(start)):
# #         if start[x] == 'A':
# #             start[x] = 'B'
# #         elif start[x] == 'B':
# #             start.append('A')
# #     tmp_k += 1
# #
# # cnt_a = 0
# # cnt_b = 0
# # for x in range(len(start)):
# #     if start[x] == 'A':
# #         cnt_a += 1
# #     elif start[x] == 'B':
# #         cnt_b += 1
# # print('{} {}'.format(cnt_a, cnt_b))

K = int(input())
lst_a = [1, 0]
lst_b = [0, 1]
for i in range(2, K+1):
    new_a = lst_a[i-1] + lst_a[i-2]
    lst_a.append(new_a)
    new_b = lst_b[i-1] + lst_b[i-2]
    lst_b.append(new_b)
print('{} {}'.format(lst_a[K], lst_b[K]))
