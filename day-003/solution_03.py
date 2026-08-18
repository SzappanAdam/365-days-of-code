def first_unique_character(text):
    uniques = {}

    for char in text:
        if char in uniques:
            del uniques[char]
        else:
            uniques[char] = 1

    if not uniques:
        return None
    return next(iter(uniques))

print(first_unique_character("swiss"))
print(first_unique_character("leetcode"))
print(first_unique_character("aabbcc"))
print(first_unique_character("a"))
print(first_unique_character(""))
print(first_unique_character("aabbc"))
print(first_unique_character("programming"))
print(first_unique_character("aabcaa"))
print(first_unique_character("aaabc"))