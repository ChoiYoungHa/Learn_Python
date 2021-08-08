# 기본 내장함수 설명

age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))


# 기본적인 함수를 정의하는 방법 default 인자값 설정

def test(a, b="name"):
    return a + b

print(test("hello", " sara"))
