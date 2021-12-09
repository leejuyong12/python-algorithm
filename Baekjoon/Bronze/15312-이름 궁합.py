import sys
sys.stdin = open('이름궁합.txt')

cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = list(input())
B = list(input())

lst = []
for x in range(len(A)):
    lst.append(cnt[ord(A[x])-65])
    lst.append(cnt[ord(B[x])-65])
# ---------------------------------------- 획수를 저장

while len(lst) > 2:
    res = []
    for i in range(len(lst)-1):
        new_a = (lst[i] + lst[i+1]) % 10  # 1의 자리
        res.append(new_a)
    lst = res
result = str(lst[0]) + str(lst[1])
print(result)