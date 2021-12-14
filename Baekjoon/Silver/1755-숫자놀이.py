import sys
sys.stdin = open('숫자놀이.txt')

M, N = map(int, input().split())
dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
lst = []
for i in range(M, N+1):
    text = ''.join(dic[c] for c in str(i))      # 이 코드 생각하기 어렵다  ******중요
    lst.append([i, text])
lst.sort(key=lambda x:x[1])     # 2번째 요소로 정렬하겠다. ******중요
for x in range(len(lst)):
    if x % 10 == 0 and x != 0:
        print()                 # 10개씩 출력
    print(lst[x][0], end = ' ')

# text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# lst = []
# for x in range(M, N+1):
#     num_text = []
#     if x >= 10:
#         num_text.append(text[x//10])
#         num_text.append(text[x % 10])
#     else:
#         num_text.append(text[x])
#     lst.append(num_text)
# lst.sort()
# fin_lst = []
# for x in range(len(lst)):
#     for y in range(len(lst[x])):
#         fin_num = ''
#         if len(lst[x][y]) == 1:
#             fin_lst.append(text.index([text[x][y]))
    # if len(lst[x]) >= 2:
    #     print(text.index(text[x][0]), text.index(text[x][1]), end='')
    # else:
    #     print(text.index(text[x]), end=' ')
# M, N = map(int, input().split())

# text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# lst = []
# for num in range(M, N+1):
#     lst.append(num)
#
# base = []
# b = []
# for x in lst:
#     # a = ''
#     if x < 10:
#         a = text[x]
#         base.append(a)
#     # b = []
#     if x > 10:
#         base.append((text[x // 10], text[x%10]))
#         # b.append(text[x % 10])
#         # base.append(b)
# base.sort()
# print(base)
# print(b)

