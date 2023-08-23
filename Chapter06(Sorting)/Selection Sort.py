# -*- coding: utf-8 -*-
#Selection Sort(���� ����): 
#�����Ͱ� �������� ���� ��, ���� ���� ���� �����͸� �����Ͽ� �� �� �����Ϳ� �ٲٰ�, 
#�״��� ���� �����͸� ������ �տ��� �ι�° �����Ϳ� �ٲٴ� ������ �ݺ�
#�ܼ��� ���� ���� �տ������� ä���ִ´�.

#���� �ڵ�(�������� ����)

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #array�� ���̸�ŭ ���� �ݺ�
    min_index=i #for���� ���� �������� ���� �۾ƾ� �ϴ� index(i��° index�� ���� ���� ���� �;� ��)
    for j in range(i+1,len(array)):#���� ���� ���� �;� �ϴ� index�� ������ ���������� ���� ���� ���� ã�´�.
        if array[min_index]>array[j]:
            min_index=j #i��° index���� �� ���� ���� �ִٸ� min_index�� ����
    array[i],array[min_index]=array[min_index],array[i]# Swap

print(array)



#Selection Sort Time Complexity
#N-1����ŭ ���� ���� ���� ã�Ƽ� ������ ������ ��=> N+(N-1)+ ...+2 = N x (N+1)/2 = O(N^2)