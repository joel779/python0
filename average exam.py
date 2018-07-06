def average(no1,no2,no3):
    if (no1 <0 or no1 >100 
        or no2 <0 or no2 >100
        or no3 <0 or no3 >100):
        print("Invalid Mark")
    else:
        average=(no1+no2+no3)/3.0
        if average>=65:
            print(average,"Pass")
        else:
            print(average,"Fail")
    
        
no1=int(input("Enter Maths grade: "))
no2=int(input("Enter English grade: "))
no3=int(input("Enter ICT grade: "))
average(no1,no2,no3)


