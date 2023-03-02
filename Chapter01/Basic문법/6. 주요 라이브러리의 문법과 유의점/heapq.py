#heapq
#힙(Heap)기능을 제공하는 라이브러리(우선순위 큐 기능을 구현하기 위해 사용)
#Min Heap을 제공한다=> O(NlogN) (Min Heap의 최상단 원소는 항상 '가장 작은' 원소

import heapq

def min_heapsort(iterable):
    h=[]
    result=[]

    for value in iterable:
        heapq.heappush(h,value) #heap에 원소를 넣는 method

    for _ in range(len(h)):
        result.append(heapq.heappop(h)) #heap에서 원소를 빼는 method
    return result

def max_heapsort(iterable):
    h=[]
    result=[]

    for value in iterable:
        heapq.heappush(h,-value) #Max Heap은 따로 구현되어 있지 않기 때문에 value값에 -를 붙여준다.

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result1=min_heapsort([1,3,5,7,9,2,4,6,8,0])
result2=max_heapsort([1,3,5,7,9,2,4,6,8,0])
print(result1)
print(result2)



