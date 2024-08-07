def count(s):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0
    for ch in s:
        if ch.isalpha():  
            if ch in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return num_vowels, num_consonants
string = input("Enter a string: ")
vowels, consonants = count(string)
print("Number of vowels:" vowels)
print("Number of consonants:" consonants)
