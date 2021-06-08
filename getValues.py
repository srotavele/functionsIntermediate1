#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(first_name):
    for s in students:
        print(s[first_name])
        


iterateDictionary2('first_name')
print("==" *5)

def iterateDictionary2(last_name):
    for s in students:
        print(s[last_name])


iterateDictionary2('last_name')
