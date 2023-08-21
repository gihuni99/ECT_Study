#itertools
#반복되는 형태의 데이터를 처리하는 기능을 제공(순열과 조합 라이브러리를 제공)
#제공하는 클래스 중 대표적인 것: permutations, combinations

#permutations: iterable object에서 r개의 data를 뽑아 일렬로 나열하는 모든 경우(순열 P)를 계산
from itertools import permutations

data=['A','B','C']
result=list(permutations(data,3)) #data에서 3개를 뽑아 나열하는 모든 경우를 반환
print(result)

#combinations: iterable object에서 r개의 data를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합 C)를 계산
from itertools import combinations

result=list(combinations(data,2))
print(result)

#product: permutations처럼 순열을 계산하지만, 원소를 중복하여 뽑는다.
from itertools import product

result=list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

#combinations_with_replacement: combinations처럼 조합을 계산하지만, 원소를 중복하여 뽑는다.
from itertools import combinations_with_replacement

result=list(combinations_with_replacement(data,2))
print(result)


