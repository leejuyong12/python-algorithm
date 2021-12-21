import sys
sys.stdin = open('생태학.txt')
from collections import defaultdict
trees = defaultdict(int)
cnt = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    else:
        trees[tree] += 1
        cnt += 1

sorted_trees = sorted(trees.items(), key=lambda x:x[0])
for key, value in sorted_trees:
    ans = round((value/cnt)*100, 4)
    print(key, '%.4f' %ans)


