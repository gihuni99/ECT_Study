# -*- coding: utf-8 -*-
#파이썬의 장점을 살린 Quick Sort

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:#리스트가 하나 이하의 원소를 가지고 있다면 종료
        return array

    pivot=array[0]
    tail=array[1:]#pivot을 제외한 리스트

    #Partition
    left_side=[x for x in tail if x<=pivot] #pivot보다 작은 왼쪽 부분
    right_side=[x for x in tail if x>pivot] #pivot보다 큰 오른쪽 부분

    #분할 이후 각각 sort
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
