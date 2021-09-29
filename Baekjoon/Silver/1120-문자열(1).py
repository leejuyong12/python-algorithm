A, B = map(str, input().split())

result = []
# 문자의 길이가 같을 때
if len(A) == len(B):
    cnt = 0
    for x in range(len(A)):
        if A[x] != B[x]:
            cnt += 1
    result.append(cnt)

# 문자의 길이가 다를 때 -> 새로운 문자를 추가할 필요없이 그냥 있는 그대로 브루트포스 방법으로 각각 다 비교
elif len(A) < len(B):           # 왜냐하면 새롭게 추가하는 문자는 비교하는 문자와 같은걸 추가하기 때문에 무조건 동일
    diff = len(B) - len(A)
    for x in range(len(B)-len(A)+1):
        cnt = 0
        for y in range(len(A)):
            if A[y] != B[x+y]:
                cnt += 1
        result.append(cnt)
print(min(result))                  # 최솟값

# ex) azc 와 xyabcxy 비교
# azc   azc   azc   azc   azc
# xya   yab   abc   bcx   cxy
#  3     3     1     3     3    - 다른 갯수(result 안에 들어있는 것)