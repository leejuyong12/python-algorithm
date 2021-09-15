import sys
sys.stdin = open('2304-백준-창고다각형.txt')

def mymax(lst):
    max_num = 0
    max_id = 0
    for i in range(len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            max_id = i
    return max_num, max_id

N = int(input())
lst = [0] * 1001

for n in range(N):
    L, H = map(int, input().split())

    lst[L] = H
area = 0

max_num, max_id = mymax(lst)    # 최대 높이, 최대 높이를 가진 인덱스
# print(max_num)                # 10이 나온다. 제일 높은 높이가 max_num
# print(max_id)                 # 8이 나온다. max_num의 인덱스
max_h = 0   # max_num 과 똑같이 높이를 지칭
for i in range(max_id+1):   # max_id까지
    if max_h >= lst[i]:     # 만약에 max_h가 그대로 크다면
        area += max_h       # area에 그 면적의 넓이를 그대로 더해준다

    else:                   # 새로운 max_h 가 나타난다면
        max_h = lst[i]      # max_h 는 그 높이로 바뀌고
        area += max_h       # 그 면적의 넓이를 더해준다

max_h2 = 0                # 여기부터는 중간에 높은 높이가 나오그 그 다음부터 그거 보다 작은 높이가 나올때 맨 뒤부터 시작
for j in range(1000, max_id, -1):   # 1000부터 오는 이유는 1001개의 마지막 인덱스는 1000(헷갈렸음), 앞에서 max_id가 8이었다. max_id-1로 하지않고 이렇게 해야 제일 높은 곳이 포함되지 않는다.
    if max_h2 >= lst[j]:            # 여기부터는 앞에와 똑같은 논리이다.
        area += max_h2
    else:
        max_h2 = lst[j]
        area += max_h2
print(area)
