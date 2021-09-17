TEXT = list(input().upper())
set_TEXT = list(set(TEXT))      # set으로 그대로 두면
lst = []
for x in set_TEXT:
    lst.append(TEXT.count(x))

if lst.count(max(lst)) >= 2:
    print('?')
else:
    max_text = set_TEXT[lst.index(max(lst))]        # 여기서 오류가 난다.
    print(max_text)                                 # set은 분절할 수 없다.







# max_text = TEXT[0]
# max_cnt = TEXT.count(TEXT[0])
# for x in range(1, len(TEXT)):
#     if TEXT[x] != max_text:
#         if TEXT.count(TEXT[x]) == max_cnt:
#             max_text = '?'
#             break
#         elif TEXT.count(TEXT[x]) > max_cnt:
#             max_text = TEXT[x]
#             max_cnt = TEXT.count(TEXT[x])
#
# print(max_text)

