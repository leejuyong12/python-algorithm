def solution(s):
    p_cnt = 0
    y_cnt = 0

    for x in s:
        if x == 'p' or x == 'P':
            p_cnt += 1
        elif x == 'y' or x == 'Y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False