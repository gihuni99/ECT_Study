##########for문############
#for 변수 in 리스트:
#   실행할 코드
#EX1)
result=0

for i in range(1,10): #i는 1부터 9까지의 모든값 순회
    result+=i

print(result)

#EX2)
score=[90,85,77,65,97]

for i in range(5):
    if score[i]>=80:
        print(i+1,"번 학생은 합격입니다.")

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)

