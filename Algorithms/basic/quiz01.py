def is_palindrome(word):
    a = ''.join(list(reversed(word)))
    if word == a:
        return "ture"
    else:
        return "false"


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))