# 내가 풀었당
# 슬라이싱 활용
# abc를 문자열로 바꿨기 때문에 다시 if 조건문에서 int로 바꿔줘야 x 와 같은지 비교 가능

a = int(input())
b = int(input())
c = int(input())

abc = str(a * b * c)

for x in range(10):
    cnt = 0
    for y in range(len(abc)):
        if x == int(abc[y]):
            cnt += 1

    
    print(cnt)