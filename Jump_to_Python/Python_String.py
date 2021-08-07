# 인덱스 슬라이싱 기준 [이상:미만:간격]
a = "2020110031Rainy"
print(a[:8])  # 0이상 8미만
print(a[::1])  # 처음부터 끝까지 한칸간격
print(a[::2])  # 처음부터 끝까지 두칸 간격
print(a[::-1])  # 뒤에서부터 1개씩
print("--------------------")

# 문자열 포맷팅
number = 10
day = "three"
b = "I eat %d Apple. so I was sick for %s days" % (number, day)
print(b)
print("this is {0}".format("kimchi"))
print("this is {name} {age}".format(name="kimchi", age=20))
print(f"this is {day}")
print("--------------------")

# 정렬과 공백
c = "%10s" % "hi"
print(c)
print("--------------------")

# 소수점 자르기
d = "%0.4f" % 3.4213423
print(d)
print("--------------------")

# 문자열 함수 사용하기
e = "hobby"
print(e.count('b'))  # b의 개수를 카운트함.
print(e.find('b'))  # b의 문자열 인덱스를 리턴함. 없으면 -1이 나옴

f = ",".join("abcd")  # ","문자열 기준으로 뒤의 문자를 쪼개서 조인을하겠다 라는의미
print(f)
g = "  Hellomm  "  # 양쪽 공백지우기
print(g.strip())

aa = "Life is too short"
print(aa.replace("Life", "Your leg"))  # Life라는 문자를 변경한다.
print(aa.split())  # 공백단위로 나누어 리스트로 만들어준다.
print("--------------------")

# 리스트
abc = ["babel", "pull down", "let pull down", [1, "Babel", 3]]
print(abc[0])
print(abc[3])
print(abc[3][1])  # 리스트안의 리스트의 1번째 요소를 가져와라
abc[0:2] = ["change", "develop"]
print(abc)
abc[0:2] = []
print(abc)
del abc[1]
print(abc)
print("--------------------")

# 리스트 함수
uu = ["kimchi", "bit", "coin", "dDL"]
uu.sort()  # 정렬
print(uu)
uu.reverse()  # 문자열 뒤집기
print(uu)
print(uu.index('bit'))  # 정렬하고 뒤집은 후 bit의 index
uu.insert(0, "append")
print(uu)
uu.remove('append')  # remove는 삭제하고자하는 값을입력
print(uu)
uu.extend([2, 3])  # 제일 끝에 리스트추가
print(uu)








