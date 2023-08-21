# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기 <= 오름차순으로 정렬하는 command가 존재
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
#Ex) [6, 4, 3, 5]에 k가 3이라면 큰 수의 법칙에서 하나의 배열은 [6, 6, 6, 5]이다.
#즉 k+1이 배열 하나의 길이
# 가장 큰 수가 k만큼 나오고, 두번째로 큰 수가 1번 나와야 하므로
count = int(m / (k + 1)) * k #배열의 총 개수 x k = 가장 큰 수가 더해지는 횟수
count += m % (k + 1)#마지막에 완성되지 못한 배열은 모두 가장 큰 수로 이루어져 있기 때문에 나머지 연산으로 count 계산

result = 0
result += (count) * first # 가장 큰 수 더하기(count는 가장 큰 수가 나오는 횟수)
result += (m - count) * second # 두 번째로 큰 수 더하기(m에서 가장 큰 수가 나오는 횟수를 빼면 두 번째로 큰 수가 나오는 횟수)

print(result) # 최종 답안 출력
