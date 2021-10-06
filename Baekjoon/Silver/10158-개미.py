w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

arr = [[0]*w for _ in range(h)]

for x in range(w):
    for y in range(h):
        for z in range(t):
            if x == w-1 or y == h-1:

            arr[p-1][q-1]