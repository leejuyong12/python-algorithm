import sys
sys.stdin = open('팰린드롬 만들기.txt')

S = input()
lst = [0] * 26
for s in S:
    lst[ord(s)-65] += 1
check = 0
tmp = ''
ans = ''
for x in range(len(lst)):
    if lst[x] % 2 == 1:
        check += 1
        tmp = chr(x+65)
    ans += chr(x+65) * (lst[x] // 2)

lst_ans = list(ans)
lst_ans.reverse()
if check > 1:
    print("I'm Sorry Hansoo")
else:
    print(ans + tmp + ''.join(map(str, lst_ans)))