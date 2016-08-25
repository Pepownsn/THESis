#### FUNCTION
'''
test
'''
#define function: def 'name'(): add:
def  example():
    print('basic function')
    z = 3 + 6 + 9 + 12 +15
    print(z)
example()

### Function Parameter
def simple_addition (num1,num2):
    answer = num1 + num2
    print 'num1 is',num1
    print answer
simple_addition(7.5,10)
simple_addition(num2 = 10,num1 = 80) ##type2
##not ok : simple_addition(num1 = 10)

#global & local
x = 6
def example1():
    global x    ##add to use x in function
    x += 5
    print(x)
example1()

## not ok : def example2():
##    print (x)
##    x += 7
##    print (x)
## example2()

def example3():
    print x    ##value of x is changed (6 to 11)
    sum = x
    sum += 20
    print sum
example3()
