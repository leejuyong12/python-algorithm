# a e i o u 하나를 반드시 포함
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다

# 민기님 풀이 참고

def check(text):
    vowel = ['a', 'e', 'i', 'o', 'u']
    text = list(text)
    cnt = 0
    for i in range(len(vowel)):
        if vowel[i] in text:       # 모음 체크
            cnt += 1
    if cnt == 0:
        return 0

    for i in range(len(text)-2):       # 모음 3개 연속되면 안된다
        if text[i] in vowel and text[i+1] in vowel and text[i+2] in vowel:
            return 0                # 자음 3개 연속되면 안된다
        if text[i] not in vowel and text[i+1] not in vowel and text[i+2] not in vowel:
            return 0

    for i in range(len(text)-1):
        if text[i] == text[i+1]:    # 같은 글자 연속된거 판단하기
            if text[i] == 'e' or text[i] == 'o':    # e나 o는 허용
                continue
            else:
                return 0
    return 1

while True:
    text = input()
    if text == 'end':
        break
    if check(text) == 1:
        print('<{}> is acceptable.'.format(text))
    else:
        print('<{}> is not acceptable.'.format(text))