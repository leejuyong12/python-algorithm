TC = int(input())

for tc in range(1, TC+1):
    text = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for x in range(len(text)):
        if text[x] not in vowels:
            result += text[x]
    print('#{} {}'.format(tc, result))