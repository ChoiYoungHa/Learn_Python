# 들여쓰기를 중요시한다 tab 으로 꼭 구분해주기

money = True
arr = [1, 2, 3]

if 1 in arr:  # not in 1이 arr 에 없어야 true // in 1이 arr 에 있어야 true
    print("택시를 타고 가라")
    print("aa")
else:
    print("걸어가라")

# 성공일 때 조건을 먼저 써주고, 그다음에 조건식을 써준다.
result = 'off'
score = 60
result = 'success' if score >= 60 else 'false'
print(result)
print('-------------------')

# while 문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 {}번 찍었습니다.".format(treeHit))
    if treeHit == 10:
        print("나무가 넘어갑니다.")

coffee = 10
coffee_money = 0

while coffee > 0:
    print("커피를 판매합니다.")
    coffee -= 1
    coffee_money += 1000
    print("남은 커피의 양은 {}입니다.".format(coffee))
    if not coffee:  # 커피가 없다면 실행
        print("커피가 품절 되었습니다.")
        print("오늘의 수입 : %d" % coffee_money)
        break

print("---------------")

# for 문

test_list = ['one', 'two', 'three']
for i in test_list:  # list 의 값을 하나하나 씩 빼온다.
    print(i)

a = [(1, 2), (3, 4), (5, 6)]  # for 문은 어떤 값이 있으면 그 값들을 하나씩 빼는 형태로 돌아감
for (first, last) in a:
    print(first + last)

mark = [90, 25, 80, 60, 40]
number = 0

for marks in mark:  # mark 배열에서 하나씩 빼고 marks 에 넣는다.
    number = number + 1
    if marks >= 60:
        print("{}학생은 합격입니다.".format(number))
    else:
        print("%d학생은 불합격입니다." % number)

# for 문의 range 는 1 ~ 10 까지의 리스트를 생성하고 in이 그것을 하나씩 빼는거다. 그래서 리스트처럼 1, 11 해주어야 1 ~ 10임.
# 1 ~ 10 까지의 합을 구함
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 간단하게 구구단
for i in range(2, 10):
    for k in range(1, 10):
        print(i * k, end=" ")
    print('')

print("--------------------")
# List 내포

a = [2, 4, 6, 7, 9]
rst = [num * 3 for num in a if num % 2 == 0]
print(rst)

double_for = [i * j for i in range(2, 10) for j in range(1, 10)]
print(double_for)


