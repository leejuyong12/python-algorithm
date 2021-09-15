# 이건 내가 생각해낸 코드가 아니여서 다시 생각해보자.

A = int(input())
B = int(input())
C = int(input())

abc = list(str(A*B*C))  # 여기서 str을 활용해 문자열로 바꿔주는게 핵심

for x in range(10):
  print(abc.count(str(x)))   # count 함수 잘 알아두자