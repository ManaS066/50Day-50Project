student_score={
    'merry': 81,
    'ron':78,
    'shyam':99,
    'hari':74,
    'ram':62
}
student_grade={}
for key in student_score:
    mark=student_score[key]
    if mark>90:
        student_grade[key]="outstanding"
    elif mark<90 and mark>75:
        student_grade[key]="good"
    elif mark<75 and mark>50:
        student_grade[key]="avg"
    elif mark<50:
        student_grade[key]="poor"
print(student_grade)