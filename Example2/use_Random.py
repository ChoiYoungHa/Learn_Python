from random import randint, uniform
# 중복제거 난수 구하기
# numbers []
# number = randint(1, 10)
#     if number not in numbers:
#         numbers.append(number)
#         print(number)

print(randint(1, 10))
print(uniform(1, 0))

i = 0
count = 0
while i < 50:
    number = randint(1, 10)
    if number == 10:
        count = count + 1
    print(number)
    i = i+1

per = count / 50

print(f"10이 나올 확율은 {per}%입니다.")
