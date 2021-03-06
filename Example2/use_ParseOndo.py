# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    temp = round((fahrenheit - 32) * 5 / 9, 2)
    return temp


# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

i = 0
while i < len(sample_temperature_list):
    sample_temperature_list[i] = fahrenheit_to_celsius(sample_temperature_list[i])
    i = i+1

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))