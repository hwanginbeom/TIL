import sys
import collections
import math

input = sys.stdin.readline
# my_str = str(int(input()))
my_str = '99991236'
list_value=[]
for i in range (0,10):
    list_value.append(my_str.count(str(i)))

list_value[9] = math.ceil((list_value[9]+list_value[6])/2)
list_value[6] = list_value[9]
print(list_value)
# print(list_value[9]+list_value[6])
print( max(list_value) )

