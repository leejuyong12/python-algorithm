A, B, C = map(int, input().split())

if B >= C:           # 가변비용(B)이 판매가격(C)보다 높거나 같으면 당연히 수익이 나지 않는다.
    print(-1)
else:
    print(  int(A/(C-B)+1)  )