def solution(n):
    lst = list(str(n))
    answer = []

    for x in range(len(lst) - 1, -1, -1):
        answer.append(int(lst[x]))
    return answer

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))