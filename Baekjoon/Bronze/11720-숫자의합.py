import sys
sys.stdin = open('11720-백준-숫자의합.txt')

t = int(input())
nums = list(map(int, input()))
print(sum(nums))
