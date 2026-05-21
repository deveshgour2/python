obtained_marks = float(input("enter the marks obtained: "))
total_marks = int(input("enter total marks: "))

if(obtained_marks > total_marks):
    print("invalid input ")

else:
    percentage = (obtained_marks / total_marks) * 100
    print("percentage = ",  percentage,"%")

    if(percentage>=90):
        print("Grade: A+")

    elif(percentage>=80):
        print("Grade: A")

    elif(percentage>=70):
        print("Grade: B")
    
    elif(percentage>=60):
        print("Grade: C")

    elif(percentage>=50):
        print("Grade: D")
    
    elif(percentage>=40):
        print("Grade: E")

    else:
        print("fail")

