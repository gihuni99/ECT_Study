# -*- coding: utf-8 -*-

#Quick Sort(�� ����):
#���� �����͸� �����Ͽ� ���غ��� ū �����Ϳ� ���� �������� ��ġ�� �ٲ۴�
#Pivot(�ǹ� ���� ���)
#1. ù��° �����͸� pivot���� ����
#2. ���ʿ������� pivot���� ū �����͸� ã��, �����ʿ������� pivot���� ���� �����͸� ã�´�.
#3. ū �����Ϳ� ���� �������� ��ġ�� ���� ��ȯ
# �ݺ��ϴٺ��� ���ʿ��� ����� �񱳱��� �����ʿ��� ����� �񱳱��� �����ϴ� ������ �ִ�.
# �ش� �������� ���������Ϳ� pivot�� ��ġ�� ����
# => ��������� pivot���� ���� ���� pivot�� ���ʿ�, ū ���� pivot�� �����ʿ� ��ġ�Ͽ� ���ҵȴ�.(Divide �Ǵ� Partition)
# ���� ���ҵ� ������ ���տ��� ���ο� pivot�� �����Ͽ� 1-3�� ������ �ݺ��Ѵ�.

#��� �Լ��� �����ϰ� ������ �� �ִµ�, ���� ������ ���� list�� ���Ұ� 1���̸� ����

#���� �ڵ�)

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end: #���Ұ� 1���̸� ����
        return
    pivot=start
    left=start+1 #left�� pivot���� ū ���� ã�´�.
    right=end #right�� pivot���� ���� ���� ã�´�.

    while left<=right: #left�� ��ġ�� right���� ���� ������, �� �����ϱ� ������ �ݺ�

        #pivot���� ū �����͸� ã�� ������ �ݺ�
        while left<=end and array[left]<=array[pivot]:# pivot���� ū ���� ã���� end�� �����ϱ� ������ while��
            left+=1

        #pivot���� ���� �����͸� ã�� ������ �ݺ�
        while right>start and array[right]>=array[pivot]:
            right-=1

        if left>right:#left�� right�� �����ȴٸ� ���� ������(right)�� pivot�� ��ȯ
            array[right],array[pivot]=array[pivot],array[right]
        else: #left�� right�� �������� �ʾҴٸ� ���� ������(right)�� ū ������(left)�� ��ȯ
            array[left],array[right]=array[right],array[left]

    #Divide(�Ǵ� Partition) ���Ŀ� ���ʰ� �����ʿ� ���� Sorting ����
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

print(array)
quick_sort(array,0,len(array)-1)
print(array)