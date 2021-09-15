# 알파벳을 숫자로 변환하기
# input ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 아스키코드 ord는 문자를 숫자로, chr은 숫자를 문자로

X = input()

for a in X:
    print(ord(a)-64, end = ' ')