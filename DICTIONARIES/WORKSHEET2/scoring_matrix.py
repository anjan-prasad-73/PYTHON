students = ['Rahul', 'Rohan']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]

score_dict = {student: {subject: scores[i][j] for j, subject in enumerate(subjects)} for i, student in enumerate(students)}

print(score_dict)
