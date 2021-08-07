# 현재 환율은 1달러 당 1000원, 1000엔 당 8달러입니다.
# 이 정보를 이용해서 파라미터 won으로 한국 금액을 받고 미국 금액을 리턴해주는 krw_to_usd 함수와,
# 파라미터 dollars로 미국 금액을 받고 일본 금액을 리턴해주는 usd_to_jpy 함수를 쓰세요. 그리고 이
# 함수들을 활용해서 아래에 원(￦)으로 정리된 amounts리스트를 달러($) 리스트와 엔(￥) 리스트로 변환 시켜보세요.

# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    return won / 1000


# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    return dollars * 125


# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i = i+1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i = i+1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))
