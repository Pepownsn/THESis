import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
88888888
'''
print exampleString
ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

##dictionaries

ageDict = {}
x = 0
for eachname in names:
    print x
    ageDict[eachname] = ages[x]
    x+=1
    print x,ageDict
print ageDict
