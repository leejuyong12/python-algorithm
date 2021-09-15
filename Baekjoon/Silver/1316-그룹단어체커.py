import sys
sys.stdin = open('1316-백준-그룹단어체커.txt')

TC = int(input())
text = [input() for _ in range (TC)]

cnt = TC
for x in range(TC):
  for y in range(len(text[x])-1):
    if text[x][y] == text[x][y+1]:
      pass
    elif text[x][y] in text[x][y+1:]:
      cnt -= 1
      break
print(cnt)