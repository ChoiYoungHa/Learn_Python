# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
i = 0
while i < 10:
    numbers.append(i+1)
    i = i + 1
print(numbers)

# numbers에서 홀수 제거
# 앞에서부터 홀수를 제거하게되면 1번째가 0번째가되고 한칸 씩 밀려서 인덱싱하기 헛갈림
# 그래서 뒤에서부터 인덱싱을하면 앞에는 홀수제거의 영향을 받지 않았기에 인덱싱이 안밀림
# 그래서 뒤에서부터 하나씩 제거하는거
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 != 0:
        del numbers[i]
    i = i-1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
print(sorted(numbers))