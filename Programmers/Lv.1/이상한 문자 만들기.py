# upper 와 lower도 있다.

def solution(s):
    lst = s.split(' ')
    ans = ''
    for x in range(len(lst)):
        for y in range(len(lst[x])):
            if y % 2 == 0:
                if 97 <= ord(lst[x][y]) <= 122:
                    ans += chr(ord(lst[x][y])-32)
                else:
                    ans += lst[x][y]
            else:
                if 65 <= ord(lst[x][y]) <= 90: 
                    ans += chr(ord(lst[x][y])+32)
                else:
                    ans += lst[x][y]
        if x == len(lst)-1:
            break
        ans += ' '
    return ans
# def toWeirdCase(s):
#     a=[]
#     s=s.split(" ")
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j%2==0:
#                 a.append(s[i][j].upper())
#             else:
#                 a.append(s[i][j].lower())
#         a.append(" ")
#
#     c="".join(a[:-1])
#     return c
#
# print("결과 : {}".format(toWeirdCase("try hello world")));