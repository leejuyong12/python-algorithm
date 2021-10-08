M, N = map(int, input().split())

text = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lst = []
for num in range(M, N+1):
    lst.append(num)

base = []
b = []
for x in lst:
    # a = ''
    if x < 10:
        a = text[x]
        base.append(a)
    # b = []
    if x > 10:
        base.append((text[x // 10], text[x%10]))
        # b.append(text[x % 10])
        # base.append(b)
print(sorted(base))
# print(b)