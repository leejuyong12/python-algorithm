import sys
sys.stdin = open('2116-주사위쌓기-백준.txt')

TC = int(input())

for tc in range(1, TC+1):
    A, B, C, D, E, F = list(map(int, input().split()))

    # 처음 제일 큰 값을 갖는 인덱스 찾고 인접하는 것들 중 작은 값 찾아 그 값의 인덱스 반환
    # 그 인덱스에 위치한 값과 똑같은 값을 갖는 것을 두번째 주사위에서 찾자.
    # 그 값의 인덱스를 반환하여