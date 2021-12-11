import sys
sys.stdin = open('직사각형에서탈출.txt')

x, y, w, h = map(int, input().split())

print(min(abs(x-w), x, abs(y-h), y))