def is_anagram(text1, text2):
    char_count = {}
    if len(text1) != len(text2):
        return False

    for char in text1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in text2:
        if char in char_count:
            char_count[char] -= 1
        else:
            char_count[char] = -1

    for char in char_count.keys():
        if char_count[char] != 0:
            return False
    return True


print(is_anagram("listen", "silent")) # True
print(is_anagram("anagram", "nagaram")) # True
print(is_anagram("rat", "car")) # False
print(is_anagram("a", "a")) # True
print(is_anagram("a", "b")) # False
print(is_anagram("", "")) # True
print(is_anagram("abc", "ab")) # False
print(is_anagram("ab", "abc")) # False
print(is_anagram("aabbcc", "abcabc")) # True