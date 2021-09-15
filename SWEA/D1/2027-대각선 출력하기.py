# 쉽게 print만 써서 출력할 수 도 있지만 그걸 의도한 문제는 아닌 것 같아 다른 방법을 생각해봤다.

for x in range(5):
    for y in range(5):
      if x == y:
          print('#', end = '')  # x와 y가 같을때 #을 출력
      else:
          print('+', end = '')  # x와 y가 다르면 +를 출력
    print('\n')                 # 한줄한줄 넘기기