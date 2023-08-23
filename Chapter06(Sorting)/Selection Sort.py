# -*- coding: utf-8 -*-
#Selection Sort(선택 정렬): 
#데이터가 무작위로 있을 때, 그중 가장 작은 데이터를 선택하여 맨 앞 데이터와 바꾸고, 
#그다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복
#단순히 작은 값을 앞에서부터 채워넣는다.

#예시 코드(오름차순 정렬)

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #array의 길이만큼 연산 반복
    min_index=i #for문을 도는 시점에서 가장 작아야 하는 index(i번째 index에 가장 작은 값이 와야 함)
    for j in range(i+1,len(array)):#가장 작은 수가 와야 하는 index를 제외한 나머지에서 가장 작은 수를 찾는다.
        if array[min_index]>array[j]:
            min_index=j #i번째 index보다 더 작은 값이 있다면 min_index에 저장
    array[i],array[min_index]=array[min_index],array[i]# Swap

print(array)



#Selection Sort Time Complexity
#N-1번만큼 가장 작은 수를 찾아서 앞으로 보내야 함=> N+(N-1)+ ...+2 = N x (N+1)/2 = O(N^2)