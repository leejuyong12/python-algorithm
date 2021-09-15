def check(str0):
    # str 이 회문이면 True:
    # 아니면 False
    #lst = []
    #lst_reverse = []

#    for ARR in range(len(str)):
 #       lst.append(str[ARR])
  #  for ARR_RE in range(len(str)-1, -1, -1):
   #     lst_reverse.append(str[ARR_RE])

#    if lst == lst_reverse:
 #       return True
    st = 0
    ed = len(str0) -1
    while st < ed and str0[st] == str0[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return True
    return False

def CC():
    #회문을 찾아서 return
    #가로
    for row in range(N):
        for st in range(N-M+1):
            result_r = check(arr[row][st:st+M])
            if result_r:
                return arr[row][st:st+M]

    #세로
    for column in range(N):
        for st in range(N-M+1):
            temp_str = ''
            for k in range(st, st+M):
                temp_str += arr[k][column]
            result_c = check(temp_str)
            if result_c:
                return temp_str

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result_final = CC()
    print('#{} {}'.format(tc, result_final))