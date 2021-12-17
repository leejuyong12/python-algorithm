import sys
sys.stdin = open('듣보잡.txt')

N, M = map(int, sys.stdin.readline().split())
listen = set(sys.stdin.readline().rstrip() for _ in range(N))   # 입력값 받는법 sys 쓰니까 엄청 빨라진다.
see = set(sys.stdin.readline().rstrip() for _ in range(M))      # rstrip() 써야하는거 생각하기

result = list(listen & see)         # 이런 코드가 있는 줄 처음알았고(교집합 구하기 &)
print(len(result))
result.sort()
for x in result:
    print(x)