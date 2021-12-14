import sys
sys.stdin = open('소트인사이드.txt')

N = list(input())
N.sort(reverse=True)

for x in range(len(N)):
    print(N[x], end='')