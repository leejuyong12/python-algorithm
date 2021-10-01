import sys
sys.stdin = open('조교 성적 매기기.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, K = map(int, input().split())

    student = N // 10                   # 1
    major = ['A+', 'A0', 'A-',
             'B+', 'B0', 'B-',
             'C+', 'C0', 'C-',
             'D0']

    total_score = []
    for n in range(N):
        A, B, C = map(int, input().split())

        score = A * 0.35 + B * 0.45 + C * 0.2
        total_score.append(score)

    score_k = total_score[K-1]
    # print(score_k)                      # 92.550000
    total_score.sort(reverse=True)          # 내림차순 정렬

    result = total_score.index(score_k) // student      # 비율 적용

    print('#{} {}'.format(tc, major[result]))

