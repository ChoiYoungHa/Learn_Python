a = 1  # 첫번재 값
b = 0  # 두번재 값

i = 0  # 증가값
# 피보나치
while i < 20:  # 20번반복
    print(a)
    temp = b  # a를 출력하고 a를 오른쪽으로 옮겨야하는데 그대로 옮기면 b가 덮어 씌워지니 temp에 보관
    b = a  # temp 보관 후 b가 비었으니 a 이동
    a = b + temp  # a가 b로 갔으니 b는 a고, temp 는 b이다. 그 둘을 합하면 새로운 수가 생김
    i = i + 1
