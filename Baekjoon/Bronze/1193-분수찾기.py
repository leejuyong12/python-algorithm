X = int(input())
# 직접 그려보면서 규칙을 찾아야 한다.
line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X
print('{}/{}'.format(a,b))
