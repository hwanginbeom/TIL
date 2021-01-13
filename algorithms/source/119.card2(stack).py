
import sys

a = int(sys.stdin.readline())


array = list(range(1, a+1))

for i in range(0,a-1):
    array.pop(0)
    array.append(array[0])
    array.pop(0)
print(array[0])