# -*- coding: utf-8 -*-
#����) N���� �л� ����(�̸�, ����)�� �ִ�.
#�� �л��� ������ �־����� ��, ������ ���� ������� �л��� �̸��� ����Ͻÿ�

n=int(input())

array=[]

for i in range(n):
    #array.append(tuple(input().split())) #�ش� �ڵ嵵 ����������, �̷��� �Ǹ� �ڿ� �ԷµǴ� ���ڵ� string������ ����.
    data=input().split()
    array.append((data[0],int(data[1])))

def setting(data):
    return data[1]

array.sort(key=setting) # data=sorted(array,key=setting) �� ����

for j in range(n):
    print(array[j][0],end=' ')