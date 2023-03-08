#- 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
#(단, 2번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.)

#1. N에서 1을 뺀다.
#2. N을 K로 나눈다.

#- Ex) N이 17, K가 4라고 가정
#1번의 과정을 한번 수행하면 N=16, 이후에 2번의 과정을 두번 수행하면 N은 1이 된다.
#⇒전체 과정을 실행한 횟수는 3(N을 1로 만드는 최소 횟수)
#- N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오
#[조건]
#첫째 줄에 N(2≤N≤100000)과 K(2≤K≤100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

N,K=map(int,input().split())
result=0 #연산량을 저장하는 변수
Km=1 #K의 제곱값을 저장하는 변수
count1=-1 #실제보다 한번 더 연산을 하므로 -1에서 시작, N을 K로 나누어주는 연산 횟수
while Km<=N: #K의 제곱값인 Km이 N보다 작거나 같으면(이후과정에서 K로 한번 나누어주기 때문) Km에 K를 곱해준다.
    Km*=K
    count1+=1
Km/=K #Km이 N보다 커졌을 때 While문이 멈추기 때문에, K를 한번 나누어주어야 N보다 작은 K의 제곱 값이 나온다.
count2=N-Km #K로 나누는 연산이 가능한 K의 제곱값 Km을 만들기 위해 1을 빼는 연산을 해주어야 하는데, 그 횟수를 의미한다.
#위는 count2=N%Km으로 대체해도 상관 없다.

result=int(count1+count2)

print(result)

