marks = [10, 11, 20, 30, 60, 90]
marks.reverse
grade = list(map(lambda x: 'A' if x >= 90 else( 'B' if x >= 60 else ('C' if x >= 30 else 'F')), marks))
print(grade)
