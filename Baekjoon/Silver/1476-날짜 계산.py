E, S, M = map(int, input().split())

tmp_E, tmp_S, tmp_M = 1, 1, 1
cnt = 1

# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19
while True:
    if E == tmp_E and S == tmp_S and M == tmp_M:
        break
    tmp_E += 1
    tmp_S += 1
    tmp_M += 1
    cnt += 1
    if tmp_E > 15:
        tmp_E -= 15
    if tmp_S > 28:
        tmp_S -= 28
    if tmp_M > 19:
        tmp_M -= 19
print(cnt)