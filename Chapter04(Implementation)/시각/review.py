# -*- coding: cp949 -*-

h=int(input("hour: "))

count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #if i==3 or j==3 or k==3: #�̷��� �ڵ��ϸ� 30�� ������ ���� �ʴ´�.
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)