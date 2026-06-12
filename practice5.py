def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
score = int(input("Enter your score: "))
grade = check_grade(score)
print(f"The grade for a score of {score} is: {grade}")