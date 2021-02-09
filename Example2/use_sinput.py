from calculator import *

num = int(input("정수를 입력하세요 : "))
a, b = map(int, input("두 수를 입력하세요 : ").split())

print(sum(num, 20))
print(f"동시에 같이 받은 수의 합은 {a + b}")
