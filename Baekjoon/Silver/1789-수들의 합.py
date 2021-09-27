S = int(input())            # 200

n = 1
result = 0
while True:
    result += n
    if result >= S:     # 넘어가거나 같은 순간 바로 break
        break
    else:
        n += 1          # 연속되는 자연수
# print(result)     # 210이 나온다.
if result > S:      # 200의 예로 들면 이거 다 더하면 210인데 10만 빼면 200이 되는거니까 1개만 빼면 된다.
    print(n-1)
elif result == S:   # 같으면 그대로 출력 , else: 를 써도 된다.
    print(n)