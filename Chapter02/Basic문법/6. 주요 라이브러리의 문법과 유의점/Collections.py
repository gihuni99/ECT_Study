#Collections
#Deque, Counter 등 유용한 자료구조를 포함하는 라이브러리

#Deque
#popleft():첫번째 원소 제거/pop():마지막 원소 제거
#appendleft(x):첫번째 index에 원소 x삽입/append(x):마지막 index에 원소 x 삽입
#모든 연산이 O(1)이다.(리스트에서 가장 앞쪽 원소 추가는 O(N))
from collections import deque

data=deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) #리스트 자료형으로 변환 가능

#Counter
#iterable object에서 원소가 몇번 등장했는지 알려준다.
from collections import Counter

counter=Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # dictionary 자료형으로 변환