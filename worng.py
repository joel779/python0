animal1=(input("enter first aniaml : "))
animal2=(input("enter second animal : "))
if animal1 < animal2:
    animal1first = True
else:
    animal1first = False

if animal1first:
    print(animal1 + " comes before " + animal2)
else:
    print(animal1 + " comes after " + animal2)
