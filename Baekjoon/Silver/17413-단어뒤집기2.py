import sys
sys.stdin = open('단어뒤집기2.txt')
# 아이디어 참고
S = list(input())
i = 0
while i < len(S):
    if S[i] == '<': # < 이게 나오면
        i += 1      # 계속 탐색하다가
        while S[i] != '>':  # > 이게 나올때까지
            i += 1          # 계속 탐색
        i += 1          # 이 과정이 끝나면 다음거부터 또 탐색
    elif S[i].isalnum():    # isalnum은 알파벳이나 숫자인지
        tmp_i = i           # 임시로 i 저장해주고
        while i < len(S) and S[i].isalnum():
            i += 1
        tmp = S[tmp_i:i]     # tmp는 그 단어 추출
        tmp.reverse()        # 그리고 그거 reverse
        S[tmp_i:i] = tmp     # 이걸 본래에 다시 넣어주기
    else:
        i += 1               # 그 외에는 다 계속 탐색
print(''.join(S))
