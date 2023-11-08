student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for name, score in student_scores.items():
    if score <= 70:
        grade = "Fail"
    elif score <= 80:
        grade = "acceptable"
    elif score <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[name] = grade
    
print(student_grades)