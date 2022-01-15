import sys
sys.stdin = open('서강근육맨.txt')

N = int(input())
scary = list(map(int, input().split()))
scary.sort()
scary_length = len(scary)
# 1 3 4 7 9 -> 9
# 1 3 4 7  -> 8
# 2 5 6 8 9 10
max_num = 0
for x in range(scary_length//2):
    # if scary_length % 2 == 0:
    #     num = scary[x] + scary[scary_length-(x+1)]
    #     if max_num < num:
    #         max_num = num
    if scary_length % 2 == 0:
        max_num = max(max_num, scary[x] + scary[scary_length-(x+1)])
    else:
        max_num = max(max_num, scary[x] + scary[scary_length-1-(x+1)], scary[-1])
print(max_num)