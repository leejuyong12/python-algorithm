import sys
sys.stdin = open('단순 2진 암호코드.txt')

pat = ['0001101',  # 0
       '0011001',  # 1
       '0010011',  # 2
       '0111101',  # 3
       '0100011',  # 4
       '0110001',  # 5
       '0101111',  # 6
       '0111011',  # 7
       '0110111',  # 8
       '0001011'   # 9
        ]

def find_start(N, M):
    for i in range(N):  # 패턴의 끝
        for j in range(M-1, 54, -1):
            if arr[i][j] == '1':
                return (i, j)
def f(N, M):
    i, j = find_start(N, M)     # 패턴의 오른쪽 끝
    j -= 55     # 패턴의 시작 인덱스
    pwd = []
    for _ in range(8):  # 8개의 암호숫자 찾기
        for k in range(10):
            if pat[k] == arr[i][j:j+7]:
                pwd.append(k)       # pat의 인덱스가 암호숫자
                j += 7
    # 유효한 암호인지 확인
    ans = 0
    if ((pwd[0] + pwd[2] + pwd[4] + pwd[6]) * 3 + pwd[1] + pwd[3] + pwd[5] + pwd[7])%10 == 0:
        ans = sum(pwd)
    return ans


TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print('#{} {}'.format(tc, f(N, M)))