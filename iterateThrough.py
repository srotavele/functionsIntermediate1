#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


# def iterateDictionary(students):
#     for student in students:
#         print(f"%s - %s, %s - %s" % (list(student)
#               [0], student['first_name'], list(student)[1], student['last_name']))
def iterateDictionary(students):
    for i in students:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
       

iterateDictionary(students)
