import sys
sys.stdin = open('이름궁합.txt')

cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = list(input())
B = list(input())

lst_a = []  # 1 2 2
lst_b = []  # 3 3 2
lst_sum = []
for x in range(len(A)):
    lst_a.append(cnt[ord(A[x])-65])
    lst_b.append(cnt[ord(B[x])-65])
# ---------------------------------------- 획수를 저장


