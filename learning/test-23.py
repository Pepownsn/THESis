## MATPLOT
import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
# plt.plot ([5,6,7,8],[7,3,8,3])
# plt.show()

# y = [1,2,3,4,5,6,7,8,9]
# x = [1,2,3,4,5,6,7,8,9]
#
# x2 = [5,6,7,8]
# y2 = [7,3,8,3]
# print(len(x))  #print dimension of vector X
# print(len(y))

x,y = np.loadtxt('exampleFile.csv',
                 unpack=True,
                 delimiter = ',')

plt.plot(x,y,'r')

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
'''
# plt.plot(x,y)
# plt.scatter(x,y,'color',)

# plt.plot(x,y,'g',linewidth=5)
# plt.plot(x2,y2,'c',linewidth=1)

# plt.plot(x,y,'g',label='line one', linewidth=1)
# plt.plot(x2,y2,'c',label='line two',linewidth=1)

# x = [5,8,10]
# y = [12,16,6]
#
# x2 = [6,9,11]
# y2 = [6,15,7]
#
# plt.bar(x,y,align='center')
# plt.bar(x2,y2,color = 'g',align='center')

plt.legend()
plt.grid(True,color='r')
plt.show()
'''
