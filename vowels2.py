word=str(input("Enter word: "))


vowels=("a","e","i","o","u")
count = 0
for char in word:
 if char in vowels:
    count = count+1
print("Number of vowels in word = ",count)


