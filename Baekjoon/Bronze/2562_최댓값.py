

lst = []
for x in range(9):
    a = int(input())
    lst.append(a)

print(max(lst))
print(lst.index(max(lst))+1)   # index 활용!!, +1 해주는 것도 확인 !!