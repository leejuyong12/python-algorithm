# n개의 꼭짓점을 가진 다각형에서 4개의 점을 고르면 사각형 하나를 만들 수 있다.
# 그 사각형은 하나의 꼭짓점을 가진다. 그러므로 몇개의 사각형을 만들 수 있는지 구하면 된다.
# nC4
def factorial(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num

N = int(input())
print(factorial(N)// (factorial(N-4) * factorial(4)))
