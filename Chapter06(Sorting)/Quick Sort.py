# -*- coding: utf-8 -*-

#Quick Sort(퀵 정렬):
#기준 데이터를 설정하여 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다
#Pivot(피벗 개념 사용)
#1. 첫번째 데이터를 pivot으로 설정
#2. 왼쪽에서부터 pivot보다 큰 데이터를 찾고, 오른쪽에서부터 pivot보다 작은 데이터를 찾는다.
#3. 큰 데이터와 작은 데이터의 위치를 서로 교환
# 반복하다보면 왼쪽에서 출발한 비교군과 오른쪽에서 출발한 비교군이 교차하는 지점이 있다.
# 해당 지점에서 작은데이터와 pivot의 위치를 변경
# => 결과적으로 pivot보다 작은 것은 pivot의 왼쪽에, 큰 것은 pivot의 오른쪽에 위치하여 분할된다.(Divide 또는 Partition)
# 이후 분할된 각각의 집합에서 새로운 pivot을 설정하여 1-3의 과정을 반복한다.

#재귀 함수로 간결하게 구현할 수 있는데, 종료 조건은 현재 list의 원소가 1개이면 종료

#예시 코드)

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end: #원소가 1개이면 종료
        return
    pivot=start
    left=start+1 #left는 pivot보다 큰 수를 찾는다.
    right=end #right는 pivot보다 작은 수를 찾는다.

    while left<=right: #left의 위치가 right보다 작을 때까지, 즉 교차하기 전까지 반복

        #pivot보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:# pivot보다 큰 수를 찾으며 end에 도달하기 전까지 while문
            left+=1

        #pivot보다 작은 데이터를 찾을 때까지 반복
        while right>start and array[right]>=array[pivot]:
            right-=1

        if left>right:#left와 right가 엇갈렸다면 작은 데이터(right)와 pivot을 교환
            array[right],array[pivot]=array[pivot],array[right]
        else: #left와 right가 엇갈리지 않았다면 작은 데이터(right)와 큰 데이터(left)를 교환
            array[left],array[right]=array[right],array[left]

    #Divide(또는 Partition) 이후에 왼쪽과 오른쪽에 대해 Sorting 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

print(array)
quick_sort(array,0,len(array)-1)
print(array)