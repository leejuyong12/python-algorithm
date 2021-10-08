def partitionH(l, r):
    p = l
    i = l + 1
    j = r

    while i < j:    # 이때 동안 밑에거를 다 돌려라

        while i < r and lst[i] <= lst[p]:
            i += 1

        while j > l and lst[j] >= lst[p]:
            j -= 1

        if i < j:
            lst[i], lst[j] = lst[j], lst[i]


    # 위의 while 문 끝나면 i j 역전된 상태
    lst[p], lst[j] = lst[p], lst[j]
    return j

def partitionL(l, r):
    p = r
    i = l-1
    for j in range(l, r):
        if lst[j] < lst[p]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[i+1] = lst[i+1], lst[p]
    return i+1