#############집합(set) 자료형###################
#특징: 중복을 허용하지 않는다, 순서가 없다(인덱싱으로 값을 얻을 수 없다)->시간복잡도: O(1)
#dictionary에서 key값이 없고 value값만 존재한다고 생각하면 될 것 같다.
#Set(집합) 자료형 초기화 방법1
data=set([1,1,2,3,4,4,5]) #숫자가 중복되지만, 출력해보면 중복되지 않는다.
print(data)

#Set(집합) 자료형 초기화 방법2
data={1,1,2,3,4,4,5}
print(data)

##########집합 자료형의 연산############
a=set([1,2,3,4,5])
b=set([3,4,5,6,7])

print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

#############집합 자료형 관련 함수##############
data=set([1,2,3])
print(data)

data.add(4) #집합 데이터에 값을 추가
print(data)
data.update([5,6]) #집합 데이터에 값을 여러개 추가
print(data)
data.remove(3) #특정값(3)을 갖는 원소 삭제
print(data)



