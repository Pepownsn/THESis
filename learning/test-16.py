## list manipulation
x = [5,6,2,1,6,7,2,2,5,6,7,2]

x.append(8888)    ##insert this no. in the last digit
print(x)

x.insert(2,99)  ##instead no. 99  in the 2-digit
print(x)

x.remove(7)  ##remove no. 7 first you see
print(x)

print (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
x.remove(x[5])  ##iremove no. as same as x[5] in the first seen
print(x)
print (x[-1])
print (x[-4])
print (x[-2])
print (x[5:8]) ##equalto 5 but leaa than 8
print(x.index(2)) ## fing the index of no.  2 (only first one index)
print(x.count(2)) ## count the no. of  2 in this range

x.sort() ##arrage the no.
print x

y= x.sort()
print (y) ##SHOW NONE

y = ['jane','Bob','pepo','joe','alice']
print(y[4])
y.sort()
print y
