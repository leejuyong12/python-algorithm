import sys
sys.stdin = open('이진검색트리.txt')
sys.setrecursionlimit(10 ** 9)
def postorder(start, end):
    if start > end:     # 재귀 두번째 postorder 식 관련해서 start가 더 크면 아무것도 반환 x
        return

    root = preorder[start]
    tmp = end + 1       # 나눌지점 일단 tmp로 생성
    for i in range(start+1, end+1):
        if root < preorder[i]:      # root값보다 큰 값이 나오면 오른쪽 탐색하기 위해
            tmp = i                 # 그때의 i값 적용
            break
    postorder(start+1, tmp-1)   # root 기준 왼쪽
    postorder(tmp, end)       # root 기준 오른쪽
    print(root)


preorder = []
while True:         # 입력받는거 확인하기!!
    try:
        n = int(input())
    except:
        break
    preorder.append(n)

postorder(0, len(preorder)-1)