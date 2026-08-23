def is_palindrome(text):
    clean = ""
    if not text:
        return True

    for char in text:
        if char.isalnum():
            clean += char
    clean = clean.lower()

    i = 0
    j = len(clean) - 1 
    while i < j:
        if clean[i] != clean[j]:
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