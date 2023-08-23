# -*- coding: utf-8 -*-
#���̽��� ������ �츰 Quick Sort

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:#����Ʈ�� �ϳ� ������ ���Ҹ� ������ �ִٸ� ����
        return array

    pivot=array[0]
    tail=array[1:]#pivot�� ������ ����Ʈ

    #Partition
    left_side=[x for x in tail if x<=pivot] #pivot���� ���� ���� �κ�
    right_side=[x for x in tail if x>pivot] #pivot���� ū ������ �κ�

    #���� ���� ���� sort
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
