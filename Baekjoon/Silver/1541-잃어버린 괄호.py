import sys
sys.stdin = open('잃어버린괄호.txt')

# 0번 인덱스에 위치한 것은 무조건 더해줘야한다. why? 처음에는 숫자로 시작하니까 음수가 나올 수 없음

math_expression = input().split('-')
res = 0
for x in math_expression[0].split('+'): # 0번 인덱스니까 더해주기.
    res += int(x)
for x in math_expression[1:]:
    for y in x.split('+'):
        res -= int(y)
print(res)