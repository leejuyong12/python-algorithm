TC = int(input())
for tc in range(1, TC+1):
    number, text = map(str, input().split())
    new = ''
    for x in text:
        for y in range(int(number)):
            new += x
    print(new)