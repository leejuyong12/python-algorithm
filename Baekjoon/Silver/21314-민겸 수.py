import sys
sys.stdin = open('민겸수.txt')

# minkyum = input()
# # 작은건 K가 나오면 그 전에 끊어주기
# # M -> K 면 1
# # M -> M 면 10
# # K -> K 면 5
# min_val  = ''
# i = 0
# while i < len(minkyum)-1:
#     if minkyum[i] == 'M':
#         if minkyum[i+1] == 'K':
#             min_val += '1'
#         elif minkyum[i+1] == 'M':
#             min_val += '10'
#             i += 1
#     elif minkyum[i] == 'K':
#         min_val += '5'
#     i += 1
#
# print(min_val)
# 큰건 K가 한번 나오면 끝
minkyum = input().rstrip()

n = len(minkyum)
max_v = ''
left = 0
for i in range(n):
    if minkyum[i]=='K':
        max_v += '5' + '0'*(i - left)
        left = i+1
if minkyum[n-1] =='M':
    max_v += '1'*(n - left)

min_v = ''
left = 0
for i in range(n):
    if minkyum[i]=='K':
        if i>0 and minkyum[i-1]=='M':
            min_v += str(10**(i-left-1))
        min_v += '5'
        left = i+1
if minkyum[n-1] =='M':
    min_v += '1' + '0'*(n-1 - left)
print(max_v)
print(min_v)