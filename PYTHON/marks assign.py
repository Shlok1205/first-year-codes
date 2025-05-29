def grade_student(marks, project_submitted):

    marks = float(marks)

    if project_submitted:
        if marks > 90:
            grade = 'A+'
        elif marks >= 80:
            grade = 'A'
        elif marks >= 70:
            grade = 'B'
        elif marks >= 60:
            grade = 'C'
        else:
            grade = 'Fail'
    else:
        if marks > 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'Fail'

    return grade

marks = float(input("Enter the student's marks: "))
project_submitted = input("Was the project submitted? (yes/no): ").strip().lower() == 'yes'
print("The grade is:", grade_student(marks, project_submitted))