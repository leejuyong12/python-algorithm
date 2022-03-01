def solution(n, arr1, arr2):
    base = []
    for i in range(n):
        arr1_b = format(arr1[i], 'b')  # 2진수로 바꾸기
        arr2_b = format(arr2[i], 'b')

        sum_arr = str(int(arr1_b) + int(arr2_b))
        if len(sum_arr) < n:
            sum_arr = '0' * (n - len(sum_arr)) + sum_arr
        k = ''
        for j in range(n):
            if sum_arr[j] == '0':
                k = k + ' '
            else:
                k = k + '#'
        base.append(k)
    return base