def calculate(payment, cost):
    result = payment - cost
    five = 50000
    one = 10000
    fife = 5000
    thou = 1000

    print(f"50000원 지폐 : {result // five}장")
    result = result % five
    print(f"10000원 지폐 : {result // one}장")
    result = result % one
    print(f"5000원 지폐 : {result // fife}장")
    result = result % fife
    print(f"1000원 지폐 : {result // thou}장")


calculate(100000, 33000)
print("-------------------")
calculate(500000, 378000)




