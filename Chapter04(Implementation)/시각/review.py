# -*- coding: cp949 -*-

h=int(input("hour: "))

count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            #if i==3 or j==3 or k==3: #이렇게 코딩하면 30은 검출이 되지 않는다.
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)