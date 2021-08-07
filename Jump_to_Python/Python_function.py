# 함수

#  *args 몇개를 넣어도 다 받겠다
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 3, 5))
print("---------")


#  **kwargs 키워드가 몇개가 들어와도 다 받겠다 딕셔너리 키워드말하는 듯
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if k == "name":
            print("당신의 이름은 : " + k)


print(print_kwargs(name="int 조수", b="2"))
print("---------")


# 여러개의 값을 리턴하고 그중에 골라서 사용할 수 있다.
def sum_and_mul(a, b):
    return a + b, a * b, a - b


print(sum_and_mul(1, 2)[0])  # 튜플형태로 3개의 값이 리턴되는데 그중에 골라서 사용가능
print("---------")


# 디폴트 함수인자
def say_myself(name, old, man=True):
    print("이름은 %s" % name)
    print("나이는 %d" % old)
    if man:
        print("남자")
    else:
        print("여자")


say_myself("이름", 24, False)  # False 를 넣지 않으면 디폴트값으로 남자가 됨.
print("---------")

ho = 1


def var_test():
    global ho
    ho = ho + 1


var_test()
print(ho)
print("---------")

# 람다 함수
# def add(a,b) return a+b의 축약버전
add = lambda a, b: a + b
print(add(1, 2))

myList = [lambda a, b: a + b, lambda a, b: a * b]  # 리스트에 람다를 저장하면 이름조차 필요없이 정의가능
print(myList[1](4, 2))



