import sys
sys.stdin = open('11654-백준-아스키코드.txt')

TC = 6
for tc in range(1, TC+1):
    t = input()

    print(ord(t))
