maths_mark=int(input("Please enter mark for maths exam: "))
english_mark=int(input("Please enter mark for englush exam: "))
ict_mark=int(input("Please enter mark for ict exam: "))
average_grade(maths_mark,english_mark,ict_mark)

def average_grade (number1,number2,number3):
    if (number1 <0 or number1 >100
        or number2 <0 or number2 >100
        or number3 <0 or number3 >100):
            print("Invalid mark")
    else:
        average_mark =(number1 + number2 + number3)/3.0
        if average_mark >=65:
           print(average_mark,"Pass")
        else:
           print(average_mark,"Fail")
