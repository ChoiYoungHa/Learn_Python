# input
# a = input("숫자를 입력하세요 : ")
# print(a)

# print
print("life", "is", "too short")  # String 붙히기를 자동으로 해줌 " " + " " 또한 , 사용 시 띄어쓰기도 해줌

for i in range(1, 10):
    print(i, end=' ')  # end 사용하면 개행방지해줌 그리고 공백사이에 원하는 문자열추가 가능

# 파일 읽고 쓰기
# w 쓰기 r 읽기 a 추가
f = open("새파일.text", 'w')  # 현재 경로에 파일오픈 없다면 생성됨
f.close()

f = open("새 파일.text", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("새 파일.text", 'r', encoding='UTF-8')
line = f.readline()
print(line)
f.close()

# 여러줄 읽기
f = open('새 파일.text', 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 통채로 가져오기
f = open('새 파일.text', 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()
