###########입력(input)###########
#데이터를 입력받을 때는 input()
#Ex)
#입력받는 변수는 문자열이다. 따라서 int()를 사용하여 정수형 데이터로 바꾸어주어야 한다.
n=int(input()) #이렇게 사용하면 Enter를 입력할 때까지 입력을 받는다(구분단위가 Enter)

#map(function, iterable) 사용법
#map(적용시킬 함수, 적용할 값들[list나 튜플 같은])
#map을 list()로 감싸면 그 자체가 list가 된다.
data=list(map(int,input().split()))
#위는 입력을 받는데, .split()을 통해 공백(' ')단위로 입력받고, 그 값들을 int형 변수로 바꾸어 list로 만드는 코드이다.

data.sort(reverse=True)
print(data)

#공백을 기준으로 구분하여 적은 수의 데이터 입력
n,m,k=map(int,input().split())
print(n,m,k)

#입력의 개수가 많은 경우
#input()함수는 동작이 느리다=> sys.stdin.readline()함수를 사용(sys라이브러리)
import sys
data=sys.stdin.readline().rstrip()
print(data)

############출력(Output)#############
a=1
b=2
print(a,b) #줄바꿈 없이 출력

print(a)
print(b) #print()는 기본적으로 출력 이후 줄바꿈을 수행한다.


#오류발생 상황
answer=7

#print("정답은 "+answer+"입니다.") 단순하게 문자열과 정수를 +연산자를 이용하여 더하면 오류가 발생한다.

print("정답은 "+str(answer)+"입니다.") #1번 해결책: 정수형 변수를 문자열 변수로 바꾸어주어야 한다.
print("정답은",answer,"입니다.") #2번 해결책: (,)로 구분하여 출력(의도치 않은 공백 만들 수 있다)
print(f"정답은 {answer}입니다.") #python 3.6이상부터 f-string문법 사용 가능
