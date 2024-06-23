def count_vowels_and_consonants(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.lower() in vowels:
            vowel_count += 1
        elif char.lower() in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

s = "Hello, world!"
vowel_count, consonant_count = count_vowels_and_consonants(s)

print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")