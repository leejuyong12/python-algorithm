import sys
sys.stdin = open('[반복문3] 문자삼각형1.txt')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    base = [[0]]
    text = 65
