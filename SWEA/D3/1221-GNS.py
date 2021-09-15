TC = int(input())

all_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, TC + 1):
    t = input()
    numbers = list(map(str, input().split()))

    counts = [0] * 10

    for x in range(10):
        for number in range(len(numbers)):
            if all_number[x] == numbers[number]:
                counts[x] += 1

    result = ''
    for num in range(10):
        result += (all_number[num] + ' ') * counts[num]
    print('#{}'.format(tc))
    print(result)