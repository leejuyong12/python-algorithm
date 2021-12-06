lst = list(map(int, input().split()))
cnt_as = 0
cnt_de = 0
for x in range(len(lst)-1):
    if lst[x+1] - lst[x] == 1:
        cnt_as += 1
    elif lst[x] - lst[x+1] == 1:
        cnt_de += 1
if cnt_as == 7:
    print('ascending')
elif cnt_de == 7:
    print('descending')
else:
    print('mixed')


# 다른 쉬운 방법 - 그냥 정렬한거랑 비교하기
# lst = list(map(int, input().split()))
# if lst == sorted(lst):
#     print('ascending')
# elif lst == sorted(lst, reverse=True):
#     print('descending')
# else:
#     print("mixed")
