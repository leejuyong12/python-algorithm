TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()

    lst_str1 = []
    for x in range(len(str1)):
        if str1[x] not in lst_str1:
            lst_str1.append(str1[x])

    dict_str = {}
    for y in lst_str1:
        dict_str[y] = 0

    for z in range(len(str2)):
        if str2[z] in dict_str.keys():
            dict_str[str2[z]] += 1

    result = 0
    for value in dict_str.values():
        if result < value:
            result = value

    print('#{} {}'.format(tc, result))