word=input("Enter a word:")
print("vowels are:")
for letter in word.lower():
    if letter in "aeiou":
        print(letter)