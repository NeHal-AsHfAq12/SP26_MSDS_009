def calculate_grade(marks):
    if marks >= 80:
        grade = "A GRADE"
    elif marks >= 70:
        grade = "B GRADE"
    elif marks >= 60:
        grade = "C GRADE"
    elif marks >= 50:
        grade = "D GRADE"
    else:
        grade = "FAIL"

    return grade  