##########사전(Dictionary) 자료형############
#키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형
data=dict()
data['사과']='Apple'
data["바나나"]='Banana'
data['코코넛']='Coconut'

print(data)

if '사과' in data:
    print("'사과'를 key로 가지는 데이터가 존재합니다.") #활용 예시


########Dictionary관련 함수###############

key_list=data.keys() #변수.keys(): key 데이터만 담은 리스트
value_list=data.values() #변수.values(): value 데이터만 담은 리스트
print(key_list)
print(value_list)

for key in key_list: #각 key값에 따른 value를 하나씩 출력하는 반복문
    print(data[key])




