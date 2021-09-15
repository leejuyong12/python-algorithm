# 2가지 방법 확인  - 2가지 방법의 차이점은 결과가 나중에 모아서 나오느냐, 즉시 나오느냐의 차이

# 내가 한 코드

T = int(input()) 
numbers = []


for a in range(T):
    num = list(map(int,input().split()))
    numbers.append(num)

for x in range(T):    # 이게 들어가냐 안들어가냐 차이
    result = 0
    for y in numbers[x]:
      if y % 2 != 0:
        result += y
        
    print('#{} {}'.format(x+1, result))


# 더 간단한 코드

T = int(input()) 

for a in range(T):
    num = list(map(int,input().split()))

    total = 0

    for nums in num:
      if nums % 2 != 0:
        total += nums
        
    print(f'#{a+1} {total}')