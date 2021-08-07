class FourCal:
    firstName = "Kim"  # 클래스 전역변수로 만들 수 있다. 공통으로 변경 됨.

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):  # 자바 클래스 this 처럼 필드값이다.
        self.first = first
        self.second = second

    def add(self):  # 필드값에 저장된 받아온 인자값들을 연산하고 리턴한다.
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):  # FourCal 객체를 상속받음.
    def div(self):
        if self.second == 0:  # 부모객체를 상속받고 부모의 div 메서드를 Override 확장했다. 우선순위는 자식메서드다.
            return 0
        else:
            return self.first / self.second


#  생성자라서 무조건 값을 넣어주어야 실행이 된다.
a = FourCal(1, 2)
print(a.add())

b = MoreFourCal(2, 0)
print(b.add())
print(b.div())  # 2 / 0 0으로 못나누게 만들어둔 메서드가 잘 동작한다.

FourCal.firstName = "Choi"
print(a.firstName)
print(b.firstName)

