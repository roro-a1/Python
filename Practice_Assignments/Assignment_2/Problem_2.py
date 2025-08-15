# The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade.
# The student gets a grade as per the following rules:
# Average Grade - 90-100 A, 80-89 B, 70-79 C, 60-69 D, 0-59 F

def student_grade(a, b, c):
    avg = (a + b + c)/3
    if avg >= 90 and avg <= 100:
        print("Grade is A. Congratulations!!")
    elif avg >= 80 and avg < 90:
        print("Grade is B")
    elif avg >= 70 and avg < 80:
        print("Grade is C")
    elif avg >= 60 and avg < 70:
        print("Grade is D")
    else:
        print("Grade F. Failed!!")

sub1 = int(input("Subject 1 marks: "))
sub2 = int(input("Subject 2 marks: "))
sub3 = int(input("Subject 3 marks: "))

student_grade(sub1, sub2, sub3)
