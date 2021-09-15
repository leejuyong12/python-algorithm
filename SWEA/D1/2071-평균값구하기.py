
# 앞으로 입력값을 각각 쪼개 무엇인가를 하려면 이렇게 하자.

T = int(input())

for a in range(T):
    lst = list(map(int, input().split()))
    

    total = 0
    avg = 0
    
    for x in numbers[a]:
        total += x
        avg = round(total / len(lst))
    print(f'#{a+1} {avg}')


# 밑의 코드에서 numbers = [], numbers.append(lst) 불필요한 단계

T = int(input())

numbers = []

for a in range(T):
    lst = list(map(int, input().split()))
    numbers.append(lst)

    total = 0
    avg = 0

    for x in numbers[a]:
        total += x
        avg = round(total / len(lst))

    print(f'#{a+1} {avg}')