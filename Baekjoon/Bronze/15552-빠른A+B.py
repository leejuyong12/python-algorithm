import sys
sys.stdin = open('15552-백준-빠른A+B.txt')


# 여기부터 답
import sys
TC = int(input())

for tc in range(TC):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# input() 대신에 sys.stdin.readline() 을 넣었다. 그리고 sys를 써주니까 답에서 import sys를 넣어줘야 함!