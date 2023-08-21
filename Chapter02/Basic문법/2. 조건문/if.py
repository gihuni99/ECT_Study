#조건문 예시
x=15

if x>=20:
    print(x)
elif x>=10:
    print('nnn')
else:
    print('sss')

#####비교연산자####
#x==y,x!=y,x>y,x<y,x>=y,x<=y
#####논리연산자####
#X and Y: X, Y가 모두 True일 때, True
#X or Y: X, Y중 하나만 True여도 True
#not X: X가 False일 때, True

#####기타 연산자#####
list='Hello World'
X='e'
if 'e' in list: #in 연산자는 list안에 'e'가 들어있으면 True
    print('True1')
if X in list:
    print('True2')
if X not in list: #not in 연산자는 list안에 X가 들어있지 않으면 True
    print('True')
else:
    print('False')

###########조건문 간단히 나타내기#########

score=85

if score>=80:
    print('시험 통과입니다.1')
else:
    print('시험 불합격입니다.1')

if score>=80: print('시험 통과입니다.2') #실행될 소스코드가 한줄일 경우 줄바꿈하지 않아도 된다.
else: print('시험 불합격입니다.2')

result="시험 통과입니다.3" if score>=80 else "시험 불합격입니다.3" # 조건부 표현식을 사용하면 if else문을 한줄에 작성 가능하다.
print(result)

print('시험 통과입니다.4') if score>=80 else print('시험 불합격입니다.4')


############추가적인 활용#############
a=[1,2,3,4,5,5,5]
remove_set={3,5}

result1=[]
for i in a:
    if i not in remove_set:
        result1.append(i)

print(result1)
#위 코드를 조건부 표현식을 활용하여 간단하게 아래와 같이 나타낼 수 있다.

result2=[i for i in a if i not in remove_set]
print(result2)



