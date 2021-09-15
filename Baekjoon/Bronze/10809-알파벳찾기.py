import sys
sys.stdin = open('10809-백준-알파벳찾기.txt')

text = input()
alpha = list(range(97, 123))    # 아스키코드!!!!

for x in alpha:
    print(text.find(chr(x)), end= ' ')  # find로 찾았는데 없으면 -1로 내보내줌