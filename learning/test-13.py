## type1
import statistics
example_list = [4,5,6,5,8,6,8,3,9,1,3,7,9,61,7,98,6,1,94,9,6]
x = statistics.mean(example_list)
y = statistics.stdev(example_list)
z = statistics.variance(example_list)
print x
print y
print z

## type2
import statistics as sta
example_list = [4,5,6,5,8,6,8,3,9,1,36,1,94,9,6]
p = sta.mean(example_list)
print p

## type3
from statistics import variance
example_list = [4,5,6,5,8,6,8,3,9,1,36,1,94,9,6]
u = variance(example_list)
print u

## type4
from statistics import variance as v
example_list = [4,5,6,5,8,6,8,3,9,1,36,1,94,9,6]
w = v(example_list)
print w

##type5
from statistics import variance as v , mean as m
example_list = [4,5,6,5,8,6,8,3,9,1,36,1,94,9,6]
w = v(example_list)
e = m(example_list)
print w
print e
