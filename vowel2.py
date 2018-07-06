word=str(input("Enter Word: "))

vowels=("a","e","i","o","u","A","E","I","O","U")
count_vowel = 0

for char in word:
 if char in vowels:
    count_vowel=count_vowel+1

print("Number of vowels in",word,"=",count_vowel)
