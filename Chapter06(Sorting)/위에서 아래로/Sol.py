# -*- coding: utf-8 -*-

#����) ������ ������������ �����ϴ� ���α׷�

#������ ���� �ִ� ���� ���� N�� �־�����(1<=N<=500)
#������ ���� 1~100,000�� �ڿ���

n=int(input())

array=[]

for i in range(n):
    array.append(int(input()))

#array.sort(reverse=True) #�� �ڵ嵵 �����ϱ�� �Ѵ�.

array=sorted(array,reverse=True)

for i in array:
    print(i,end=' ')