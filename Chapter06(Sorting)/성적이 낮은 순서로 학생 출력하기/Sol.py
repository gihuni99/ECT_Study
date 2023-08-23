# -*- coding: utf-8 -*-
#문제) N명의 학생 정보(이름, 성적)이 있다.
#각 학생의 정보가 주어졌을 때, 성적이 낮은 순서대로 학생의 이름을 출력하시오

n=int(input())

array=[]

for i in range(n):
    #array.append(tuple(input().split())) #해당 코드도 동작하지만, 이렇게 되면 뒤에 입력되는 숫자도 string형으로 들어간다.
    data=input().split()
    array.append((data[0],int(data[1])))

def setting(data):
    return data[1]

array.sort(key=setting) # data=sorted(array,key=setting) 도 가능

for j in range(n):
    print(array[j][0],end=' ')