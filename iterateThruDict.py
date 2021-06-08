#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dojo):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for l in dojo['locations']:
        print(l)
    print("==" *8)
    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for i in dojo['instructors']:
        print(i)


printInfo(dojo)
