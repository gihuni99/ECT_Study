##########사전(Dictionary) 자료형############
#키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형
data=dict()
data['사과']='Apple'
data["바나나"]='Banana'
data['코코넛']='Coconut'

print(data)

if '사과' in data:
    print("'사과'를 key로 가지는 데이터가 존재합니다.") #활용 예시