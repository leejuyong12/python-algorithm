# if 문을 어떻게 포맷팅 안에 넣을까 했는데 변수 하나 설정하면 된다는 것을 기억하자!

T = int(input())

for a in range(T):

  x, y = map(int, input().split())

  if x > y:
    i = ">"
  elif x < y:
    i = "<" 
  else:
    i = "="

  print(f'#{a+1} {i}')