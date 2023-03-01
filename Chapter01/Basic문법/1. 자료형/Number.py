#정수형(Integer)
a=1000
b=-7
print(a,b)

#실수형(Real Number)
c=5. #소수부가 0이거나
d=-.7 #정수부가 0인 소수는 0을 생략할 수 있다.
print(c,d)

e=1e9 #10의 9제곱
f=75.25e1 # (==752.5)
g=3054e-3 # (==3.054)
print(e,f,g)

#실수형에서의 오차
#컴퓨터 시스템이 수 데이터를 처리할 때 2진수를 사용(부동 소수점, Floating-point)=> 오차
a=0.3+0.6# 2수에서 0.9를 정확히 표시할 수 없다. 따라서 0.899999..로 표기(오차 발생)
print(a)
if a==0.9:
    print(True)
else:
    print(False)

#위 오차를 해결하기 위해 round()함수 이용
#round(실수형 데이터, 반올림하고자 하는 위치-1)
print(round(a,4)) #이는 a를 5번째 자리에서 반올림한다는 의미이고 0.9라는 결과가 나온다.

if round(a,4)==0.9:
    print(True)
else:
    print(False)


#수 자료형의 연산
a=7
b=3
print(a/b) #나누기 (실수형으로 나온다)
print(a%b) #나머지
print(a//b) #몫
print(a**b) #제곱
