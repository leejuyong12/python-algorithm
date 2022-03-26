import sys
sys.stdin = open('스위치켜고끄기.txt')
# 1은 스위치가 켜져있고, # 2는 꺼져있다
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 그 스위치의 상태를 바꾼다
# 즉 , 스위치가 켜져 있으면 꺼지고 꺼져있으면 켠다
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

N = int(input())
bulbs = list(map(int, input().split()))
S = int(input())
x, y = map(int, input().split())
a, b = map(int, input().split())

