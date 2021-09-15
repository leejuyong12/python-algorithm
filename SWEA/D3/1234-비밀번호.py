for tc in range(1, 11):

    num, password = map(str, input().split())

    result = []
    for te in password:
        if len(result) > 0 and te == result[-1]:
            result.pop(-1)
        else:
            result.append(te)
    result_str = ''
    for x in result:
        result_str += x
    print('#{} {}'.format(tc, result_str))