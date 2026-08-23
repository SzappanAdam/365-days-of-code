def is_palindrome(text):
    if not text:
        return True

    text = text.lower()

    i = 0
    j = len(text) - 1 
    while i < j:
        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        elif text[i] != text[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("Was it a car or a cat I saw?")) # True
print(is_palindrome("Python")) # False
print(is_palindrome("")) # True
print(is_palindrome("a")) # True