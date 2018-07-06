def exam_grade(level,mark):
    if level <1 or level>4:
        print("invalid level")

    elif mark <0 or mark >100:
        print("invalid level")

    elif level==1 or level==2:
        if mark >85:
            print("distinction")
        elif mark >=75:
            print("merit")
        elif mark >=65:
            print("pass")
        else:
            print("fail")

    elif level==3:
        if mark >=80:
            print("distinction")
        elif mark >=70:
            print("merit")
        elif mark >=60:
            print("pass")
        else:
            print("fail")

    elif level ==4:
        if mark >80:
            print("distinction")
        elif mark >=70:
            print("merit")
        elif mark >=60:
            print("pass")
        else:
            print("fail")
level=int(input("Please enter level: "))
mark=int(input("Please enter mark: "))
exam_grade(level,mark)
