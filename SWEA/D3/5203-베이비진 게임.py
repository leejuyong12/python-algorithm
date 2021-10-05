import sys
sys.stdin = open('베이비진.txt')

def check(lst):
    for i in range(10):
        if lst[i] >= 3:     # triplet
            return True
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:     # run
            return True
    return False

TC = int(input())

for tc in range(1, TC+1):
    nums = list(map(int, input().split()))

    count_A = [0] * 12      # 인덱스오류 나오지 않게 하기 위해 12로 만든다.(함수에 있는 코드에서) # 8번 line에서
    count_B = [0] * 12

    winner = 0
    for i in range(6):
        data1 = nums[i*2]
        data2 = nums[i*2+1]

        count_A[data1] += 1
        if check(count_A):
            winner = 1
            break

        count_B[data2] += 1
        if check(count_B):
            winner = 2
            break
    print('#{} {}'.format(tc, winner))