import sys
sys.stdin = open('팰린드롬만들기.txt')
# 엄청 간단한 방법
S = input()
for i in range(len(S)):     # 일단 문자열의 개수만큼 반복문 돌리고
    if S[i:] == S[i:][::-1]:    # 시작점을 다르게 해서 팰린드롬 확인 후
        print(len(S)+i)         # 만약에 1번째 인덱스부터 팰린드롬이다! 그러면 그 전의 개수만큼 추가
        break

