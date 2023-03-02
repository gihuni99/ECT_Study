#내장 함수(Built-in Function)
#print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬기능을
#포함하고 있는 기본 내장 라이브러리
#대표적으로 input(), print()가 있고, 앞서 설명하였기 때문에 생략
my_list=[1,2,3,4,5]

result1=sum(my_list) #iterable object(리스트, 딕셔너리, 튜플 등)의 합을 반환
print(result1)

result2=min(my_list)
result3=max(4,2,6,10) #iterable object(리스트, 딕셔너리, 튜플 등)이나 2개 이상의 파라미터가 들어왔을 때,
# min()은 가장 작은값을, max()는 가장 큰값을 반환
print(result2)
print(result3)

result4=eval("(3+5)*7") #eval()은 문자열 형식으로 들어온 수식을 계산한 결과를 반환
print(result4)

result5=sorted([9,1,8,5,4]) #오름차순으로 정렬
print(result5)
result6=sorted([9,1,8,5,4],reverse=True) #내림차순으로 정렬
print(result6)

#튜플의 2번째 원소를 기준으로 내림차순 정렬(아래는 원소가 튜플로 이루어진 리스트이다.)
result7=sorted([('홍길동',35),('이순신',75),('손기훈',50)],key=lambda x: x[1],reverse=True)
print(result7)

data=[9,1,8,5,4]
data.sort() #리스트와 같은 iterable 객체는 기본적으로 sort()함수를 내장-> sorted()가 아닌 sort()로 정렬 가능
print(data) #오름차순 정렬

