# -*- coding: utf-8 -*-

#Insertion Sort(삽입 정렬)
#필요할 때만 위치를 바꾸어 데이터가 거의 정렬 되어 있을 때 효율적(적절한 위치에 '삽입')
#특정 데이터가 적절한 위치에 들어가기 전, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
#두번째 데이터부터 정렬한다(이미 첫번째 데이터는 정렬되어 있다고 판단하기 때문)

#예제

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]: #비교하여 해당 데이터가 더 작으면 위치를 바꾼다(점점 앞으로 이동)
            array[j],array[j-1]=array[j-1],array[j]
        else:#더 작은 데이터를 만나면 종료
            break

print(array)

