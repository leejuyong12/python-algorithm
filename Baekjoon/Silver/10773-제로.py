K = int(input())

nums = [int(input()) for _ in range(K)]
base = []
for x in range(len(nums)):
    if nums[x] != 0:
        base.append(nums[x])
    else:
        base.pop(-1)
print(sum(base))