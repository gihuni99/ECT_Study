#list는 대괄호 안에 원소를 넣어 초기화
#쉼표(,)로 원소를 구분
#리스트의 원소에 접근할 때는 인덱스(index)값을 괄호안에 넣는다

a=[1,2,3,4,5,6]
print(a)

print(a[4])# index 4, 즉 5번째 원소에 접근

b=list() # 비어있는 리스트 선언 방법1
print(b)
c=[] # 비어있는 리스트 선언 방법2
print(c)

#리스트 초기화하는 방법(코딩테스트에서 주로 이용)
n=10
a=[0]*n
print(a)

###############################################
#리스트의 인덱싱과 슬라이싱
a=[1,2,3,4,5,6,7,8,9]

print(a[-1]) #뒤에서 첫번째 원소 출력
print(a[-3]) #뒤에서 세번째 원소 출력

a[3]=7 # 4번째 원소(index 3) 수정(인덱싱)
print(a)

a[1:4] # 2~4번째 원소 접근
print(a[1:4])

###########################################
#list comprehension(리스트 컴프리헨션)
#대괄호 안에 간단하게 조건문을 작성하여 list를 초기화하는 방법

array1=[]
for i in range(20): # array1이라는 빈 리스트의 0~19사이의 홀수값을 리스트에 넣어주는 반복문
    if i%2==1:
        array1.append(i)
print(array1)

array2=[i for i in range(20) if i%2==1] #위 반복문과 같은 역할을 한다.(list comprehension)
print(array2)

array3=[i*i for i in range(1,10)] #1부터 9까지의 수의 제곱을 리스트에 넣는 연산
print(array3)

#NxM크기의 2차원 리스트 초기화
n=3;m=4
array4=[[0]*m for _ in range(n)] # _(언더바)는 반복을 수행하되 변수값을 무시할 때 사용
print(array4)

#NxM크기의 2차원 리스트 초기화의 잘못된 예시(list comprehension을 반드시 이용해야 한다)
n=3;m=4
array5=[[0]*m]*n # _(언더바)는 반복을 수행하되 변수값을 무시할 때 사용
print(array5)

array5[1][1]=5 #3개의 리스트에서 index 1에 해당하는 원소들이 모두 5로 바뀐다.
print(array5) #내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식

##################3######리스트 관련 method################################
a=[1,4,3]
print("기본 리스트: ",a)
#변수명.append(): 리스트에 원소를 하나 삽입할 때 사용/O(1)
a.append(2) #마지막 index에 2가 삽입된다.
print("append(삽입): ",a)

#변수명.sort():오름차순으로 정렬, 변수명.sort(reverse=True):내림차순으로 정렬/ O(NlogN)
a.sort()
print("sort(오름차순 정렬): ",a)
a.sort(reverse=True)
print("sort(reverse)(내림차순 정렬): ",a)

#변수명.reverse(): 리스트의 원소의 순서를 모두 뒤집어 놓는다/ O(N)
a.reverse()
print("reverse(원소 순서 뒤집기): ",a)

#변수명.insert(삽입할 위치 인덱스, 삽입할 값): 특정한 index위치에 원소를 삽입할 때 사용/ O(N)
a.insert(2,1) # 2번 index, 즉 3번째에 1를 넣는다.
print("insert(index 2에 1 추가): ",a)

#변수명.count(특정값): 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용/ O(N)
print("count(값이 1인 데이터 개수): ",a.count(1))

#변수명.remove(특정값): 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거/ O(N)
a.remove(1) # 값을 가진 원소가 여러개면 앞에서부터 1개만 삭제된다.
print("remove(값이 1인 데이터 삭제): ",a)

# (+)특정한 값의 원소를 모두 제거하는 방법
a=[1,2,3,4,5,5,5,5]
remove_set={3,5}
result=[i for i in a if i not in remove_set] # remove_set에 원소가 포함되어 있지 않을 때만 result에 추가
print(result)

