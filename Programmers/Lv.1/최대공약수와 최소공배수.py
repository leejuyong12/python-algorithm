def solution(n, m):
    min_num = min(n, m)
    lst = [0, 0]
    for x in range(min_num, 0, -1):
        if n % x == 0 and m % x == 0:
            lst[0] = x
            break
    for y in range(1, n*m+1):
        if y % n == 0 and y % m == 0:
            lst[1] = y
            break
    return lst