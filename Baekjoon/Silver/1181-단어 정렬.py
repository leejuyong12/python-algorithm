import sys
sys.stdin = open('단어정렬.txt')

N = int(input())
lst = [input() for _ in range(N)]
set_lst = list(set(lst))            # set으로 만들어서 중복 제거

sort_lst = []
for i in set_lst:
    sort_lst.append((len(i), i))    # 일부러 문자열 길이를 넣어줌(정렬하기 위해)
result = sorted(sort_lst)           # 문자열 길이대로 정렬

for len_lst, word in result:
    print(word)

# lambda 활용
# words_num = int(input())
# words_list = []
#
# for _ in range(words_num):
#     word = str(input())
#     word_count = len(word)
#     words_list.append((word, word_count))
#
# #중복 삭제
# words_list = list(set(words_list))
#
# #단어 숫자 정렬 > 단어 알파벳 정렬
# words_list.sort(key = lambda word: (word[1], word[0]))
#
# for word in words_list:
#     print(word[0])