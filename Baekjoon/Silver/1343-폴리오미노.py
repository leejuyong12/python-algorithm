import sys
sys.stdin = open('폴리오미노.txt')

# board = input()
#
# idx = 0
# while True:
#     if idx >= len(board):
#         break
#
#     if board[idx:idx+4] == 'XXXX':
#         idx += 4
#         board = board.replace('X', 'A', 4)
#     elif board[idx:idx+2] == 'XX':
#         idx += 2
#         board = board.replace('X', 'B', 2)
#     elif board[idx] == '.':
#         idx += 1
#     else:
#         n = -1
#         break
# print(board)

# board = input()
# board = board.replace("XXXX", "AAAA")
# board = board.replace("XX", "BB")
# if 'X' in board:
#     print(-1)
# else:
#     print(board)

board = input().split('.')
for i in range(len(board)):
    if len(board[i]) % 4 == 0:
        board[i] = 'AAAA' * (len(board[i])//4)
    elif len(board[i]) % 4 == 2:
        board[i] = 'AAAA' * (len(board[i])//4) + 'BB'
res = '.'.join(board)
if 'X' in res:
    print(-1)

else:
    print(res)