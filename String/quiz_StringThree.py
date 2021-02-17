def is_palindrome(word):
    r = list(reversed(word))
    string = ''.join(r)
    if string == word:
        return "true"
    else:
        return "false"


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
