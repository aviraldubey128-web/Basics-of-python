# a function that takes a string and returns the count of vowels and
# consonants separately.

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
            return consonant_count, vowel_count
word = "aviral"
vowel, consonants = count_vowels_consonants(word)
print(vowel, consonants)


