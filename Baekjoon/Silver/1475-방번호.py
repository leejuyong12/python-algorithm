import sys
sys.stdin = open('방번호.txt')

numbers = list(map(int, input()))
# counting 정렬

base = [0] * 10

for x in range(len(numbers)):
    if numbers[x] == 6 or numbers[x] == 9:
        if base[6] >= base[9]:
            base[9] += 1
        elif base[6] <= base[9]:
            base[6] += 1
    else:
        base[numbers[x]] += 1
print(max(base))

