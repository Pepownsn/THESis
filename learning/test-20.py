## bult-in function
import time
import math
exnum1 =-5
exnum2 = 5
print(abs(exnum1))
if abs(exnum1) == abs(exnum2):
    print 'the same no.'

exList = [5,2,1,6,7]
largest = max(exList)
print(largest)
smallest = min(exList)
print(smallest)

x = 5.622
x = round(x)
print(x)
y = 5.256
y = round(y)
print(y)
y = 5.26
y = math.ceil(y)  ##import math function 
print(y)
y = 5.756
y = math.floor(y)
print(y)


#Converting a string to an integer:
intMe = 55
intMe = int(intMe)
print(intMe)
#Converting and integer to a string:
stringMe = 55
stringMe = str(stringMe)
print(stringMe)
#Converting an integer to a float:
floatMe = 55
floatMe = float(floatMe)
print(floatMe)
