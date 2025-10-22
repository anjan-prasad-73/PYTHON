students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}

print(students['Rahul']['marks']['english'])  

for name, details in students.items():
    print(name, details['marks'])

students['Simran']['marks']['science'] = 93
print(students['Simran'])
