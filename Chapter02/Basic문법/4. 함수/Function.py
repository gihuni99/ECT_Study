#########함수(Function)############
#특정 알고리즘을 수행한 결과를 반복적으로 출력할 때 유용
#구조
#def 함수명(매개변수):
#   실행할 소스코드
#   return 반환 값

#Ex)
def add(a,b):
    return a+b

print(add(3,7))

def add(a,b):
    print('함수의 결과: ',a+b) #return 없어도 된다.
add(3,7)
add(b=3,a=7) #매개변수 사용시 인자 a,b를 직접 처리하여 넣을 수 있다.(순서가 달라져도 상관없다)

########global 변수##########
c=0
def func():
    global c #global변수를 설정하면 매개변수가 없어도 계산이 되는 것을 볼 수 있다.
    c+=1

for i in range(10):
    func()
print(c)

###########람다 표현식(Lambda Express)##########
def add2(a,b):
    return a+b
print(add2(3,7)) #일반적인 add() method
print((lambda a,b: a+b)(3,7)) #lambda express로 구현한 add() method



