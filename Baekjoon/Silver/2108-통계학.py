import sys
sys.stdin = open('통계학.txt')
# Counter 안쓰고 푸는 거 생각해봤는데 그냥 그거 생각할 시간에 Counter 쓰는법 배우는게 낫다 싶어서 이거 씀
from collections import Counter
N = int(input())
lst = []

for n in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()      # sorted_lst = lst.sort() 이게 아니다. 잘못 생각했었다.
lst_sum = sum(lst)
cnt = Counter(lst).most_common(2)   # 많은거부터 상위 2개 뽑아줌
print(round(lst_sum / N))
print(lst[N//2])
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(lst)-min(lst))
