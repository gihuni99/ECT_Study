# -*- coding: utf-8 -*-

#sort(), sorted()함수
#O(NlogN)의 Time complexity를 보장

#+) 문자의 경우 아스키코드값 기준으로 정렬됨
#+) sort(reverse=True)를 사용하면 내림차순으로 정렬됨

#Ex) sorted()는 sort()와 다르게 리스트를 'return'한다.
array1=[7,5,9,0,3,1,6,2,4,8]

result=sorted(array1)#오름차순으로 정렬됨 (리스트, 딕셔너리 자료형을 입력받아도 반환값은 항상 리스트)
print(result)

#Ex2) sort()함수는 리스트가 입력되었을 때, 내부에서 정렬됨('return'하지 않는다.)
array2=[7,5,9,0,3,1,6,2,4,8]

array2.sort()
print(array2)

#Ex3) sort()와 sorted()함수는 key매개변수(함수)를 입력 받을 수 있음
# 리스트의 데이터가 튜플로 구성되어 있을 때 사용가능

array3=[('apple',2),('carrot',5),('melon',3)]

def setting(data): #입력받은 data[1]에 해당하는 값만을 반환하는 함수
    return data[1]

#둘다 가능
result=sorted(array3,key=setting)
print(result)

array3.sort(key=setting)
print(array3)