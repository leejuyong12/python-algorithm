import sys
sys.stdin = open('4659-백준-비밀번호발음하기.txt')

def checkvowel(text):
    for t in text:
        if t in vowel:
            return True
    else:
        return False

def check3(text):
    if len(text) >= 3:
        for x in range(len(text)):
            for y in range(x, len(text)-2):
                if text[y] in vowel:
                    if text[y+1] in vowel:
                        if text[y+2] in vowel:
                            return False
                if text[y] not in vowel:
                    if text[y+1] not in vowel:
                        if text[y+2] not in vowel:
                            return False
            return True

def checkeo(text):
    if len(text) >= 2:
        for x in range(len(text)):
            for y in range(x, len(text)-1):
                if text[y] == text[y+1]:
                    if text[y] == text[y+1] == 'e':
                        return True
                    elif text[y] == text[y+1] == 'o':
                        return True
                    return False
TC = 9
for tc in range(1, TC+1):
    text = list(input())
    vowel = ['a', 'e', 'i', 'o', 'u']

    text_text = ''
    for t in text:
        text_text += t

    if text_text == 'end':
        break
    if len(text) < 2:
        if checkvowel(text) == True or None:
            print('<{}> is acceptable.'.format(text_text))
        else:
            print('<{}> is not acceptable.'.format(text_text))

    if len(text) >= 2:
        if checkvowel(text) == False or checkeo(text) == False or check3(text) == False:
            print('<{}> is not acceptable.'.format(text_text))
        else:
            print('<{}> is acceptable.'.format(text_text))


# # <a> is acceptable.
# <tv> is not acceptable.
# <ptoui> is not acceptable.
# <bontres> is not acceptable.
# <zoggax> is not acceptable.
# <wiinq> is not acceptable.
# <eep> is acceptable.
# <houctuh> is acceptable.