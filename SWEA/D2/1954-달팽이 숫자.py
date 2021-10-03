TC = int(input())
for tc in range(1, TC+1):
    n = int(input())

    base = [[0] * n for _ in range(n)]

    K = n           # 임시적으로 K로 대체해서 쓰자(원본 훼손하지 않기 위해)
    direction = 1   # 첫 방향 설정(오른쪽 열 이동하기 위해)
    row = 0         # 첫 행은 0
    col = -1        # -1 로 설정하는 이유는 밑에 * 부분에서 첫 시작에 1을 적기 위해
    num = 1         # 번호 적는 것은 1부터 시작

    while True:
        # 수평으로 이동
        for x in range(K):
            col += direction            # 열 이동
            base[row][col] = num        # * 위에서 말한 거 여기서 시작
            num += 1                    # 번호가 하나씩 늘어나는거
        K -= 1                          # 수평3 수직2 수평2 수직1 수평1
        if K == 0:                      # K가 0이 되면 끝난다.
            break
        # 수직으로 이동
        for y in range(K):
            row += direction            # 행 이동
            base[row][col] = num
            num += 1                    # 번호가 하나씩 늘어나는거
        direction *= -1         # 수평이동 수직이동 한번씩 하면 다시 반대로 수평이동 수직이동 해야한다.

    print('#{}'.format(tc))
    for x in range(n):
        for y in range(n):
            print(base[x][y], end=' ')      # 리스트 형태 제거
        print()         # 행렬로 표현하기 위해
