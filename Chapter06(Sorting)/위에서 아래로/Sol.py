# -*- coding: utf-8 -*-

#문제) 수열을 내림차순으로 정렬하는 프로그램

#수열에 속해 있는 수의 개수 N이 주어진다(1<=N<=500)
#수열의 수는 1~100,000의 자연수

n=int(input())

array=[]

for i in range(n):
    array.append(int(input()))

#array.sort(reverse=True) #이 코드도 동작하기는 한다.

array=sorted(array,reverse=True)

for i in array:
    print(i,end=' ')