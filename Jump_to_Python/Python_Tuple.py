# 튜플
# 리스트와 튜플의 차이는 리스트는 인덱스의 값을 마음대로 변경이 가능했지만 튜플은 안됨.
# 볼 순 있는데 바꿔치기할 수 없다. 길이 값 고정 삭제 시 오류
t1 = (1, 2, 'a', 'b')
# del t1[0]  # 튜플은 값을 삭제할 수 없다.
# 정리 리스트 [] 튜플 () 딕셔너리 {}

#  딕셔너리
# 해시테이블, Map 과 같은 구조
diction = {'name': 'Eric', 'age': 1}  # 딕셔너리 형태
print(diction['name'])
diction['address'] = "화곡동"  # address : 화곡동 키쌍 추가
print(diction)
del diction['age']  # age 키 삭제
print(diction)
print(diction.keys())  # 딕셔너리의 키값만 불러온다.
print(diction.values())  # 딕셔너리의 벨류값만 불러온다.
print(diction.items())  # 딕셔너리의 키, 벨류를 모두 불러온다.

for i in diction.keys():  # 딕셔너리의 키값을 모두 하나씩 출력하고 싶을 때 for 문 사용
    print(i)

for k, v in diction.items():
    print("키는 : " + k)
    print("벨류는 : " + v)

# print(diction['age']) 주소로 참조하는건 해당하는 값이 없다면 오류가뜸
print(diction.get('name'))  # 똑같이 값을 가져오는건 같음
print(diction.get('age', '없다'))  # 다만 값이 없을 때 오래대신 none 을 출력함.
print(4 in diction)  # 4가 diction에 있냐 물어보는거임
print("-------------------")

# 집합 각각의 원소는 고유하다.
# 파이썬에만 있는 자료형 중복허용 X, 순서가 없다. a[0] 이렇게 접근 불가
s1 = set('Hello')  # 집합 선언
s2 = {1, 2, 3}  # 집합 선언
s3 = set([1, 2, 3])  # 집합 선언
print(s1)  # 순서가 없고, 중복을 허용하지 않는다.
print(s3)

ex01 = set([1, 2, 3, 4, 5, 3])
ex02 = set([1, 2, 3, 7, 8, 4])
print(ex01 & ex02)  # 교집합
print(ex01.intersection(ex02))  # 교집합

print(ex01 | ex02)  # 합집합
print(ex01.union(ex02))  # 합집합

print(ex01 - ex02)  # 차집합
print(ex01.difference(ex02))  # 차집합
print(ex02 - ex01)

ex01.add(10)  # 값 하나 추가
print(ex01)
ex02.update([10, 11])  # 값 여러개 추가
print(ex02)

ex02.remove(10)  # 값 삭제
print(ex02)

# 불 참, 거짓

dd = ['one', 'two', 'three']
while dd:  # 값이 있다면 true 라고 파이썬이 내부적으로 알고 있음
    dd.pop()  # while 이 돌때마다 pop 해주니 결국엔 값이 없어지면 종료
    print(dd)

# 변수
# 파이썬에서 사용하는 변수는 객체를 가르키는 것
# 변수의 다양한 할당방법을 알아보자

a = [1, 2, 3]
b = a
a[1] = 4
print(a is b)  # 현재 a,b는 같은 메모리주소를 바라보고 있다.

#  그렇기에 a, b는 변경할 때 마다 서로 참조하게 된다.
#  그렇다면 a, b를 서로 다른 주소를 바라보게 하려면?

b = a[:]  # 이렇게하면 a의 0번째부터 마지막까지 리스트를 복사해서 그대로 전달해주기에 b는 다른 주소값에
# a의 값 그대로 복사된다.
print(a is b)  # 서로 다른 주소를 바라보기에 false 가 나온다.

c, d = ('python', 'life')  # 튜플형태로 각각 할당 가능 튜플은()로 할당 가능 근데 () 생략가능

print(c)
print(d)

e = f = 'hello'  # e f 동시에 값을 할당
print(e, f)

#  tmp
g = 3
k = 5
g, k = k, g
print(g)
print(k)
