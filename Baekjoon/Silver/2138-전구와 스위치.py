N = int(input())

def switch(lst):
    for x in range(len(lst)):
        if lst[x] == '0':
            lst[x] = '1'
        else:
            lst[x] = '0'

now = list(map(int, input()))
bulbs = list(map(int, input()))

