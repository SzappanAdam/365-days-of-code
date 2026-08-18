def first_unique_character(text):
    characters = {}

    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    for char_count in characters.items():
        if char_count[1] == 1:
            return char_count[0]

print(first_unique_character("swiss"))
print(first_unique_character("leetcode"))
print(first_unique_character("aabbcc"))
print(first_unique_character("a"))
print(first_unique_character(""))
print(first_unique_character("aabbc"))
print(first_unique_character("programming"))
print(first_unique_character("aabcaa"))