#bisect
#이진 탐색(Binary Search) 기능을 제공하는 라이브러리
#bisect_left(a,x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 method
#bisect_right(a,x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 method

# Ex) 리스트 [1,2,4,4,8]이 있을 때, 새롭게 데이터 4를 삽입

from bisect import bisect_left, bisect_right #주의)bisect.py 파일에서 bisect를 import하면 오류가 발생

a=[1,2,4,4,8]
x=4

print(bisect_left(a,x))
print(bisect_right(a,x))

#값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index

a=[1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4)) #값이 4인 데이터 개수 출력

print(count_by_range(a,-1,3)) #값이 [-1,3]범위에 있는 데이터 개수 출력
