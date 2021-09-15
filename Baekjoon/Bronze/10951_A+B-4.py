# 내가 푼 방식

n = 0
while n < 5:
    A, B = map(int, input().split())
    n += 1
    print(A+B)

# 하지만 문제에서는 테스트횟수가 주어지지 않았다. 밑의 코드는 다른 사람의 코드를 가져온 것이다.
# try ~ except 구문 확인!!

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
      break