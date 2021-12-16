import sys
sys.stdin = open('접미사배열.txt')

S = list(input())
res = ''
fin = []
for x in range(len(S)-1, -1, -1):
    res = S[x] + res
    fin.append(res)
fin.sort()
for y in range(len(fin)):
    print(fin[y])