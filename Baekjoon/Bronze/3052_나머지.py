# 처음에는 for 반복문을 1번에서 쓰고 2번에서도 쓰려고 했는데 2번에서 for 반복문 안쓰는게 더 낫다. 

lst = []

for a in range(10):      # 1


    T = int(input())     # 2
    a = T % 42
    lst.append(a)
lst = set(lst)        # set 함수 활용하기

print(len(lst))       