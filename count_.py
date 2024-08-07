def count(s):
    vowels = 'aeiouAEIOU'
    num_vowels = 0
    num_consonants = 0
    for char in s:
        if char.isalpha():  
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
                
    return num_vowels, num_consonants
string = input("Enter a string: ")
vowels, consonants = count(string)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

