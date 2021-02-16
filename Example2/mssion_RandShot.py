# 번호 뽑기
from random import Random, randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    return numbers


answer = generate_numbers()
tried_count = 0
strike_count = 0
ball_count = 0

while strike_count < 3:
    init = []
    while len(init) < 3:
        temp = int(input(f"{len(init) + 1}번째 수를 입력하세요 : "))
        if temp in init:
            print("중복된 숫자입니다. 다른 숫자를 입력하세요.")
        elif temp < 0 or temp > 9:
            print("0 ~ 9 의 숫자만 입력하세요.")
        else:
            init.append(temp)
    i = 0
    strike_count = 0
    ball_count = 0
    while i < 3:
        if init[i] == answer[i]:
            strike_count = strike_count + 1
        elif init[i] in answer:
            ball_count = ball_count + 1
        i = i + 1
    print(f"s:{strike_count} b:{ball_count}")
    tried_count = tried_count + 1

print(f"축하합니다 {tried_count}번의 시도끝에 정답을 맞추셨습니다!")



