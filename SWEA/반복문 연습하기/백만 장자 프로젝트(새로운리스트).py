import sys
sys.stdin = open('백만 장자 프로젝트.txt')

# 테스트 케이스가 너무 많아서 시간이 부족해 뒤에 채점을 못한다

# 살때의 가격보다 팔때의 가격이 높을 때 판다.
# 앞에서부터 구하면 언제가 가장 높은 가격인지, 높은 가격이 나와도 앞의 가격들을 다시 불러와야 한다는 불편함이 있기 때문에 뒤에서부터 구해보자
TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    rev_lst = []                                # 리스트 순서를 반대로 하는 새로운 리스트 만들기
    for x in range(len(lst) - 1, -1, -1):
        rev_lst.append(lst[x])
    print(rev_lst)

    profit = 0
    sell_price = rev_lst[0]
    for y in range(1, len(rev_lst)):            # 파는 가격을 index가 0인 곳으로 처음에 잡기
        if rev_lst[y] < sell_price:             # 파는 가격보다 가격이 싸다면
            profit += sell_price - rev_lst[y]   # 이익(profit)에 그 차이만큼 더해주기
        elif rev_lst[y] > sell_price:           # 반대로 파는 가격보다 가격이 크다면
            sell_price = rev_lst[y]             # 그것을 파는 가격으로 재설정해주기
    print('#{} {}'.format(tc, profit))          # 가격이 같을 때는 고려 x - 파는 가격으로 설정을 안해줘도 되고 빼도 이익이 0이기 때문에
