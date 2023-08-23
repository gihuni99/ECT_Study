# -*- coding: utf-8 -*-
#Count Sort(계수 정렬)
#특정 조건이 부합할 때만 사용 가능하지만 매우 빠르다
#데이터 수가 N개, 데이터 중 최댓값이 K일 때 계수 정렬은 최악의 경우에도 O(N+K)를 보장한다
#단, 데이터의 크기 범위가 제한되어 정수 형태로 표현 가능할 떄만 사용 가능

#예시 코드)

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array)+1) #0부터 가장 큰 정수값까지의 갯수를 표시할 리스트

for i in range(len(array)): #array의 길이만큼 반복
    count[array[i]]+=1 #한번 나올 때마다 해당 index에 count추가

for i in range(len(count)):
    for j in range(count[i]):#count된 횟수만큼 출력
        print(i,end=' ')

#Count Sort가 비효율적인 경우
#Ex) 데이터가 0과 999,999 단 두개일 때-> 데이터는 2개 밖에 존재하지 않지만 리스트의 크기는 100만이 된다.(비효율적)
