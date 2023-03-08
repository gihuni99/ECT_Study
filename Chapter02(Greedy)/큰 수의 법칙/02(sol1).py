# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기 <= 오름차순으로 정렬하는 command가 존재
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰수를 K번 더하기
        if m==0: #m이 0이라면 반복문 탈출
            break
        result += first
        m-=1 #더할 때마다 1씩 빼기
    if m==0:
        break
    result+=second #두 번째로 큰 수를 한 번 더하기
    m-=1 #더할 때마다 1씩 빼기

print(result) # 최종 답안 출력

