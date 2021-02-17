x = "CodeIt"
y = "Python"

# 리스트와 비슷하게 문자 슬라이스 가능
print(x[:4])

# 리스트와 비슷하게 문자길이 사용 가능
print("-----------------------")
print(len(x))

# 하지만 x[4] = !
# 이런식으로 문자열 변경은 불가능
print("-----------------------")

# 문자열 합치기 가능
print(x + " " + y)

print("-----------------------")

a = [1, 2, 3, 4, 5]
s1 = ''
s2 = ''
s3 = ''
for x in a:
    s1 += str(x)
    s2 += ''.join(str(x))
print(s1)
print(s2)
s3 = ''.join(str(x) for x in a)
print(s3)

# 참고로 list의 원소가 문자형일 경우
a1 = ['1', '2', '3', '4', '5']
print(''.join(a1))
