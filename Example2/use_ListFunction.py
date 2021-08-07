array = [1, 2, 3, 4, 5]

print(len(array)) # 길이확인
array.append(6) # 리스트의 끝에 값 추가
print(array)

del array[2] # 2번째 인덱스 삭제
print(array)

array.insert(3, 8) # 인덱스 3번째에 8추가
print(array)

print(sorted(array)) #정렬

