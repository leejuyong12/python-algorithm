import sys
sys.stdin = open('5와6의차이.txt')

A, B = input().split()


min_A = ''
max_A = ''

min_B = ''
max_B = ''
for i in A:
    if i == '5' or i == '6':
        min_A += '5'
        max_A += '6'
    else:
        min_A += i
        max_A += i
for i in B:
    if i == '5' or i == '6':
        min_B += '5'
        max_B += '6'
    else:
        min_B += i
        max_B += i

print(int(min_A)+int(min_B), int(max_A)+int(max_B) )
