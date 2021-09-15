import sys
sys.stdin = open('2941-백준-크로아티아알파벳.txt')
# 현준님 아이디어 활용!
TC = 5
for tc in range(1, TC+1):
    cro_text = input()

    base = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for x in base:
        cro_text = cro_text.replace(x, '1')
    print(len(cro_text))

    # result = []
    #
    # if len(cro_text) >= 3:
    #     # 3글자 찾을때
    #     for x in range(len(cro_text)-2):
    #         for y in range(x, x+3):
    #             result.append(cro_text[x+y])
    #     # 2글자 찾을때
    #     for x in range(len(cro_text)-1):
    #         for y in range(x, x + 2):
    #             result.append(cro_text[x + y])
    #     # 1글자 찾을때
    #     for x in range(len(cro_text)):
    #         result.append(cro_text[x])
    #
    # if len(cro_text) == 2:
    #     for x in range(len(cro_text)-1):
    #         for y in range(x, x + 2):
    #             result.append(cro_text[x])
    #     for x in range(len(cro_text)):
    #         result.append(cro_text[x])
    #
    # if len(cro_text) == 1:
    #     for x in range(len(cro_text)):
    #         result.append(cro_text[x])
    # print(result)




