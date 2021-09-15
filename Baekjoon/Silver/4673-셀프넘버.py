# 함수로 구현하는 것보다 이게 더 편한 것 같다.
# 만약에 처음부터 set으로 만들었다면 append 대신에 add 쓰면 된다!
# set을 쓰면 set끼리 연산 가능

base_nums = list(range(1, 10001))
compare_nums = []

for x in range(1, 10001):
    for y in str(x):
        x += int(y)
    compare_nums.append(x)

base_nums = set(base_nums)
compare_nums = set(compare_nums)

final_nums = sorted(base_nums - compare_nums)
for i in final_nums:
    print(i)