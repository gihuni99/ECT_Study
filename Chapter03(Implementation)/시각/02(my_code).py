#N은 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력하시오.

N=int(input()) #N은 00시 00분 00초부터 N시 59분 59초까지의 범위를 나타낼 때 쓰는 변수
count=0 #경우의 수 저장하는 변수
for h in range(N+1):
    if h%10==3: #10으로 나누었을 때, 3이 나온다면 그 시각은 3이 들어가는 시각이다.
        count=count+3600 #만약 시간에 3이 들어간다면 그 1시간동안은 모두 3이 들어가므로 3600번의 시각이 모두 경우의 수에 해당
        continue
    for m in range(60):
        if m%10==3 or m//10==3: #나머지가 3인경우는 분단위가 3인 경우, 몫이 3인 경우는 10분단위가 3인 경우
            count=count+60
            continue
        for s in range(60):
            if s%10==3 or s//10==3:
                count=count+1
print(count)