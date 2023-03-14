# 스택은 박스 쌓기
# 선입후출, 혹은 후입선출 구조라고도 한다.

stack=[]

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5) # append와 pop method는 별도의 라이브러리가 필요없다.
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단(가장 먼저 들어간) 원소부터 출력된다.
print(stack[::-1]) #최상단(가장 나중에 들어간) 원소부터 출력된다.