import sys
sys.stdin = open('베스트셀러.txt')

N = int(input())
dic = {}
lst = []
for n in range(N):
    lst.append(input())
for x in range(N):
    dic[lst[x]] = lst.count(lst[x])

res = sorted(dic.items(), key=(lambda x: (-x[1], x[0])))    # 일단 [1] value로 내림차순 정렬한 후, [0] key로 오름차순
print(res[0][0])