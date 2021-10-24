# def factorial(N):
#     num = 1
#     for i in range(1, N+1):
#         num *= i
#     return num
#
# n, m = map(int, input().split())
#
# ans = 0
# res = str(factorial(n) // (factorial(n-m) * factorial(m)))
# for x in range(len(res)-1, -1, -1):
#     if res[x] == '0':
#         ans += 1
#     else:
#         break
# print(ans)
# 이렇게 풀었더니 시간초과가 났다.(팩토리얼로 풀면 시간초과라고 함)
# 그래서 2와 5의 개수를 통해 0을 구하여야 한다.
# 2의 개수와 5의 개수중 더 작은게 10의 개수 이다.
N, M = map(int, input().split())

def count_num(n, k):
   count = 0
   while n:
       n //= k
       count += n
   return count

cnt_five = count_num(N, 5) - count_num(M, 5) -  count_num(N-M, 5)
cnt_two = count_num(N, 2) - count_num(M, 2) -  count_num(N-M, 2)
ans = min(cnt_five, cnt_two)

print(ans)