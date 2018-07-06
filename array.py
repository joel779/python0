word=str(input("Enter word: "))

vowel=("a","e","i","o","u")

count=0

for char in word:
    if char in vowel:
        count=count+1

print("Number of vowles in",word,"=",count)
