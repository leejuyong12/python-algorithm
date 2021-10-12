import sys
sys.stdin = open('벽돌깨기.txt')
import copy


def drop(pos, BLOCKS):
    ST = []     # 스택
    # 세로 위치를 찾는다.
    row = 0
    while row < H and BLOCKS[row][pos] == 0:
        row += 1
    if row == H:
        return
    ST.append((pos, row))

    # 블럭 제거
    while ST:
        curX, curY = ST.pop()
        size = BLOCKS[curY][curX]
        BLOCKS[curY][curX] = 0
        # size기준으로 삭제해야하는 것들을 스택에 넣는다.
        for i in range(size):
            # 상
            if curY-i >= 0 and BLOCKS[curY-i][curX]:
                ST.append((curX, curY-i))
            # 하
            if curY+i < H and BLOCKS[curY+i][curX]:
                ST.append((curX, curY+i))
            # 좌
            if curX-i >= 0 and BLOCKS[curY][curX-i]:
                ST.append((curX-i, curY))
            # 우
            if curX+i < W and BLOCKS[curY][curX+i]:
                ST.append((curX+i, curY))
def clean(BLOCKS):
    for x in range(W):
        desP = srcP = H-1
        while srcP >= 0:
            if BLOCKS [srcP][x] > 0:
                BLOCKS[desP][x] = BLOCKS[srcP][x]
                desP -= 1
            srcP -= 1
        while desP >= 0:
            BLOCKS[desP][x] = 0
            desP -= 1


def solve(k, BLOCKS):
    if k == N:
        return

    for i in range(W):
        tmpBlocks = copy.deepcopy(BLOCKS)
        res[k] = i
        drop(i, BLOCKS)
        # 정리작업
        clean(BLOCKS)
        solve(k+1, BLOCKS)

        BLOCKS = copy.deepcopy(tmpBlocks)


TC = int(input())
for tc in range(1, TC+1):
    N, W, H = map(int, input().split())
    BLOCKS = [list(map(int, input().split())) for _ in range(H)]

    res = [-1] * N
    solve(0, BLOCKS)
